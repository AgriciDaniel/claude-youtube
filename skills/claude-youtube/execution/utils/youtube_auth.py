"""
YouTube API authentication manager.

Handles API key auth for public Data API v3 and OAuth 2.0 for Analytics and upload.
Input: auth_type ('api_key' | 'oauth' | 'upload'), optional credentials path
Output: authenticated googleapiclient service object OR error dict

Usage:
    python execution/utils/youtube_auth.py --check api_key
    python execution/utils/youtube_auth.py --check oauth
    python execution/utils/youtube_auth.py --authorize-upload
"""

import argparse
import json
import os
import sys
from pathlib import Path

TMP_DIR = Path.home() / ".claude" / ".tmp"
TOKEN_PATH = TMP_DIR / "youtube_oauth_token.json"
CLIENT_SECRETS_PATH = Path.home() / ".claude" / "youtube_client_secrets.json"
UPLOAD_TOKEN_PATH = TMP_DIR / "youtube_upload_oauth_token.json"
UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"


def _save_upload_credentials(credentials):
    """Persist upload credentials with owner-only file permissions."""
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
    token_fd = os.open(UPLOAD_TOKEN_PATH, flags, 0o600)
    with os.fdopen(token_fd, "w", encoding="utf-8") as token_file:
        if hasattr(os, "fchmod"):
            os.fchmod(token_file.fileno(), 0o600)
        token_file.write(credentials.to_json())
    if not hasattr(os, "fchmod"):
        os.chmod(UPLOAD_TOKEN_PATH, 0o600)


def authorize_youtube_upload():
    """Run the one-time interactive OAuth flow for video uploads."""
    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        return {
            "status": "error",
            "error": "OAuth dependencies not installed",
            "fix": "pip install google-api-python-client google-auth-oauthlib",
        }

    if not CLIENT_SECRETS_PATH.exists():
        return {
            "status": "missing",
            "error": "OAuth client secrets not found",
            "fix": f"Save OAuth client secrets to {CLIENT_SECRETS_PATH}",
        }

    flow = InstalledAppFlow.from_client_secrets_file(
        str(CLIENT_SECRETS_PATH), [UPLOAD_SCOPE]
    )
    credentials = flow.run_local_server(port=0)
    _save_upload_credentials(credentials)
    return {
        "status": "ok",
        "type": "upload",
        "scope": UPLOAD_SCOPE,
        "token_path": str(UPLOAD_TOKEN_PATH),
    }


def get_youtube_upload_service():
    """Load or refresh previously authorized upload credentials without prompting."""
    try:
        from google.auth.exceptions import RefreshError
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from googleapiclient.discovery import build
    except ImportError:
        return None, {
            "error": "OAuth dependencies not installed",
            "fix": "pip install google-api-python-client google-auth-oauthlib",
        }

    if not UPLOAD_TOKEN_PATH.exists():
        return None, {
            "error": "YouTube upload OAuth is not configured",
            "fix": (
                "Run python execution/utils/youtube_auth.py --authorize-upload "
                "once to grant the youtube.upload scope."
            ),
        }

    try:
        credentials = Credentials.from_authorized_user_file(
            str(UPLOAD_TOKEN_PATH), [UPLOAD_SCOPE]
        )
    except (OSError, ValueError) as exc:
        return None, {"error": f"Unable to read YouTube upload credentials: {exc}"}

    if not credentials.has_scopes([UPLOAD_SCOPE]):
        return None, {
            "error": "Saved OAuth credentials do not include the youtube.upload scope",
            "fix": "Run python execution/utils/youtube_auth.py --authorize-upload again.",
        }

    if credentials.expired and credentials.refresh_token:
        try:
            credentials.refresh(Request())
        except RefreshError as exc:
            return None, {"error": f"Unable to refresh YouTube upload credentials: {exc}"}
        _save_upload_credentials(credentials)

    if not credentials.valid:
        return None, {
            "error": "YouTube upload OAuth credentials are invalid or expired",
            "fix": "Run python execution/utils/youtube_auth.py --authorize-upload again.",
        }

    try:
        return build("youtube", "v3", credentials=credentials), None
    except Exception as exc:
        return None, {"error": f"Failed to build YouTube service: {exc}"}


def get_api_key():
    """Return YouTube Data API v3 key from environment or config file."""
    key = os.environ.get("YOUTUBE_API_KEY")
    if key:
        return key

    config_path = Path.home() / ".claude" / "youtube-credentials.json"
    if config_path.exists():
        with open(config_path) as f:
            data = json.load(f)
            key = data.get("api_key")
            if key:
                return key

    return None


def get_data_api_service(api_key=None):
    """Build and return YouTube Data API v3 service object."""
    try:
        from googleapiclient.discovery import build
    except ImportError:
        return None, {
            "error": "google-api-python-client not installed",
            "fix": "pip install google-api-python-client google-auth-oauthlib",
        }

    if api_key is None:
        api_key = get_api_key()

    if not api_key:
        return None, {
            "error": "YouTube API key not found",
            "fix": (
                "Set YOUTUBE_API_KEY environment variable or add to "
                "~/.claude/youtube-credentials.json as {\"api_key\": \"YOUR_KEY\"}. "
                "Get a key at https://console.cloud.google.com/apis/credentials"
            ),
        }

    try:
        service = build("youtube", "v3", developerKey=api_key)
        return service, None
    except Exception as e:
        return None, {"error": f"Failed to build YouTube service: {e}"}


def get_oauth_service(scopes=None):
    """Build YouTube Analytics API service with OAuth 2.0."""
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
    except ImportError:
        return None, {
            "error": "OAuth dependencies not installed",
            "fix": "pip install google-api-python-client google-auth-oauthlib",
        }

    if scopes is None:
        scopes = [
            "https://www.googleapis.com/auth/yt-analytics.readonly",
            "https://www.googleapis.com/auth/youtube.readonly",
        ]

    TMP_DIR.mkdir(parents=True, exist_ok=True)
    creds = None

    if TOKEN_PATH.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), scopes)
        except Exception:
            creds = None

    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            with open(TOKEN_PATH, "w") as f:
                f.write(creds.to_json())
        except Exception:
            creds = None

    if not creds or not creds.valid:
        if not CLIENT_SECRETS_PATH.exists():
            return None, {
                "error": "OAuth client secrets not found",
                "fix": (
                    f"Download OAuth 2.0 client secrets from Google Cloud Console "
                    f"and save to {CLIENT_SECRETS_PATH}. "
                    f"Guide: https://developers.google.com/youtube/analytics/registering_an_application"
                ),
            }

        try:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CLIENT_SECRETS_PATH), scopes
            )
            creds = flow.run_local_server(port=0)
            with open(TOKEN_PATH, "w") as f:
                f.write(creds.to_json())
        except Exception as e:
            return None, {"error": f"OAuth flow failed: {e}"}

    try:
        service = build("youtubeAnalytics", "v2", credentials=creds)
        return service, None
    except Exception as e:
        return None, {"error": f"Failed to build Analytics service: {e}"}


def check_auth(auth_type):
    """Check if authentication is configured and return status."""
    if auth_type == "api_key":
        key = get_api_key()
        if key:
            masked = key[:4] + "..." + key[-4:]
            return {"status": "ok", "type": "api_key", "key": masked}
        return {"status": "missing", "type": "api_key",
                "fix": "Set YOUTUBE_API_KEY env var or add to ~/.claude/youtube-credentials.json"}

    elif auth_type == "oauth":
        if TOKEN_PATH.exists():
            return {"status": "ok", "type": "oauth", "token_path": str(TOKEN_PATH)}
        if CLIENT_SECRETS_PATH.exists():
            return {"status": "needs_auth", "type": "oauth",
                    "message": "Client secrets found but no token yet. Run OAuth flow."}
        return {"status": "missing", "type": "oauth",
                "fix": f"Download OAuth client secrets to {CLIENT_SECRETS_PATH}"}

    elif auth_type == "upload":
        if UPLOAD_TOKEN_PATH.exists():
            return {
                "status": "ok",
                "type": "upload",
                "token_path": str(UPLOAD_TOKEN_PATH),
            }
        return {
            "status": "missing",
            "type": "upload",
            "fix": "Run youtube_auth.py --authorize-upload once to grant upload access.",
        }

    return {"status": "error", "message": f"Unknown auth type: {auth_type}"}


def main():
    parser = argparse.ArgumentParser(description="YouTube API auth manager")
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument("--check", choices=["api_key", "oauth", "upload"],
                        help="Check auth status")
    actions.add_argument("--authorize-upload", action="store_true",
                         help="Authorize this account for YouTube video uploads")
    args = parser.parse_args()

    if args.check:
        result = check_auth(args.check)
        print(json.dumps(result, indent=2))
        sys.exit(0 if result["status"] == "ok" else 1)
    elif args.authorize_upload:
        result = authorize_youtube_upload()
        print(json.dumps(result, indent=2))
        sys.exit(0 if result["status"] == "ok" else 1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
