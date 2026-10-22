"""
Upload one video to YouTube after an explicit caller-side approval.

Input: video file, JSON metadata file, and --approval-confirmed
Output: JSON containing the uploaded video ID and privacy status

Usage:
    python execution/upload_video.py video.mp4 --metadata-file metadata.json --approval-confirmed
    python execution/upload_video.py video.mp4 --metadata-file metadata.json --approval-confirmed --privacy-status public
"""

import argparse
import json
import mimetypes
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils.quota_tracker import check_quota, consume_quota
from utils.youtube_auth import get_youtube_upload_service

ALLOWED_METADATA_FIELDS = {
    "title",
    "description",
    "tags",
    "category_id",
    "default_language",
}
PRIVACY_STATUSES = ("private", "unlisted", "public")


def build_video_resource(metadata, privacy_status="private"):
    """Validate the supported metadata shape and build an insert resource."""
    if not isinstance(metadata, dict):
        raise ValueError("Metadata must be a JSON object")

    unknown_fields = sorted(set(metadata) - ALLOWED_METADATA_FIELDS)
    if unknown_fields:
        raise ValueError(f"Unsupported metadata field(s): {', '.join(unknown_fields)}")

    title = metadata.get("title")
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Metadata requires a non-empty string 'title'")
    if len(title) > 100:
        raise ValueError("Title must be 100 characters or fewer")

    description = metadata.get("description", "")
    if not isinstance(description, str):
        raise ValueError("'description' must be a string")
    if len(description) > 5000:
        raise ValueError("Description must be 5000 characters or fewer")

    snippet = {"title": title, "description": description}
    tags = metadata.get("tags", [])
    if not isinstance(tags, list) or any(not isinstance(tag, str) for tag in tags):
        raise ValueError("'tags' must be a list of strings")
    if tags:
        snippet["tags"] = tags

    category_id = metadata.get("category_id")
    if category_id is not None:
        if not isinstance(category_id, str) or not re.fullmatch(r"\d+", category_id):
            raise ValueError("'category_id' must be a numeric string")
        snippet["categoryId"] = category_id

    default_language = metadata.get("default_language")
    if default_language is not None:
        if not isinstance(default_language, str) or not default_language:
            raise ValueError("'default_language' must be a non-empty string")
        snippet["defaultLanguage"] = default_language

    if privacy_status not in PRIVACY_STATUSES:
        raise ValueError(f"privacy status must be one of: {', '.join(PRIVACY_STATUSES)}")

    return {"snippet": snippet, "status": {"privacyStatus": privacy_status}}


def upload_video(service, video_path, resource, notify_subscribers=False):
    """Upload a video using the resumable YouTube Data API media-upload flow."""
    from googleapiclient.http import MediaFileUpload

    mime_type = mimetypes.guess_type(str(video_path))[0] or "application/octet-stream"
    if not mime_type.startswith("video/"):
        mime_type = "application/octet-stream"
    media = MediaFileUpload(str(video_path), mimetype=mime_type, resumable=True)
    return (
        service.videos()
        .insert(
            part="snippet,status",
            body=resource,
            media_body=media,
            notifySubscribers=notify_subscribers,
        )
        .execute()
    )


def _load_metadata(metadata_path):
    try:
        with metadata_path.open(encoding="utf-8") as metadata_file:
            return json.load(metadata_file)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid metadata JSON: {exc}") from exc


def build_parser():
    parser = argparse.ArgumentParser(description="Upload an approved video to YouTube")
    parser.add_argument("video_file", type=Path, help="Path to the video file")
    parser.add_argument(
        "--metadata-file",
        type=Path,
        required=True,
        help="UTF-8 JSON file containing title and optional metadata",
    )
    parser.add_argument(
        "--approval-confirmed",
        action="store_true",
        required=True,
        help="Required: the calling app has received explicit user approval",
    )
    parser.add_argument(
        "--privacy-status",
        choices=PRIVACY_STATUSES,
        default="private",
        help="Upload visibility (default: private)",
    )
    parser.add_argument(
        "--notify-subscribers",
        action="store_true",
        help="Notify subscribers; notifications are disabled by default",
    )
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    if not args.video_file.is_file():
        print(
            json.dumps({"error": f"Video file not found: {args.video_file}"}),
            file=sys.stderr,
        )
        return 1

    try:
        metadata = _load_metadata(args.metadata_file)
        resource = build_video_resource(metadata, args.privacy_status)
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 1

    quota = check_quota("videos.insert")
    if not quota.get("can_execute", False):
        print(
            json.dumps({"error": quota.get("error", "Upload quota unavailable")}),
            file=sys.stderr,
        )
        return 1

    service, error = get_youtube_upload_service()
    if error:
        print(json.dumps(error), file=sys.stderr)
        return 1

    from googleapiclient.errors import HttpError

    try:
        response = upload_video(
            service,
            args.video_file,
            resource,
            notify_subscribers=args.notify_subscribers,
        )
    except OSError as exc:
        print(json.dumps({"error": f"Unable to read video file: {exc}"}), file=sys.stderr)
        return 1
    except HttpError as exc:
        print(json.dumps({"error": f"YouTube upload failed: {exc}"}), file=sys.stderr)
        return 1

    video_id = response.get("id")
    if not video_id:
        print(
            json.dumps({"error": "YouTube upload response did not include a video ID"}),
            file=sys.stderr,
        )
        return 1

    response_status = response.get("status")
    actual_privacy_status = (
        response_status.get("privacyStatus")
        if isinstance(response_status, dict)
        else None
    )
    result = {
        "status": "uploaded",
        "video_id": video_id,
        "requested_privacy_status": args.privacy_status,
        "privacy_status": actual_privacy_status or "unknown",
    }
    if not actual_privacy_status:
        result["warning"] = "YouTube did not return the video's privacy status."
    elif actual_privacy_status != args.privacy_status:
        result["warning"] = (
            "YouTube's returned privacy status differs from the requested status."
        )
    quota_result = consume_quota("videos.insert")
    if quota_result.get("error"):
        result["quota_tracking_error"] = quota_result["error"]
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
