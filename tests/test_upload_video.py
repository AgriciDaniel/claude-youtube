import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

EXECUTION_DIR = (
    Path(__file__).resolve().parents[1] / "skills" / "claude-youtube" / "execution"
)
sys.path.insert(0, str(EXECUTION_DIR))

import upload_video


class BuildVideoResourceTests(unittest.TestCase):
    def test_builds_private_resource_by_default(self):
        resource = upload_video.build_video_resource(
            {"title": "Approved title", "tags": ["one", "two"]}
        )

        self.assertEqual(resource["snippet"]["title"], "Approved title")
        self.assertEqual(resource["snippet"]["tags"], ["one", "two"])
        self.assertEqual(resource["status"]["privacyStatus"], "private")

    def test_maps_optional_metadata(self):
        resource = upload_video.build_video_resource(
            {
                "title": "Title",
                "description": "Description",
                "category_id": "22",
                "default_language": "en",
            },
            "public",
        )

        self.assertEqual(resource["snippet"]["categoryId"], "22")
        self.assertEqual(resource["snippet"]["defaultLanguage"], "en")
        self.assertEqual(resource["status"]["privacyStatus"], "public")

    def test_rejects_invalid_or_unknown_metadata(self):
        for metadata in (
            {},
            {"title": " "},
            {"title": "Title", "category_id": 22},
            {"title": "Title", "unexpected": True},
        ):
            with self.subTest(metadata=metadata):
                with self.assertRaises(ValueError):
                    upload_video.build_video_resource(metadata)

    def test_approval_flag_is_required_by_cli(self):
        parser = upload_video.build_parser()
        with self.assertRaises(SystemExit) as error:
            parser.parse_args(["video.mp4", "--metadata-file", "metadata.json"])

        self.assertEqual(error.exception.code, 2)


class UploadVideoTests(unittest.TestCase):
    def test_calls_insert_with_resumable_media_and_no_notifications_by_default(self):
        calls = {}

        class Request:
            def execute(self):
                return {"id": "video-id"}

        class Videos:
            def insert(self, **kwargs):
                calls.update(kwargs)
                return Request()

        class Service:
            def videos(self):
                return Videos()

        media_module = types.ModuleType("googleapiclient.http")

        def fake_media_file_upload(filename, mimetype, resumable):
            calls["media_arguments"] = (filename, mimetype, resumable)
            return "media"

        media_module.MediaFileUpload = fake_media_file_upload
        with tempfile.NamedTemporaryFile(suffix=".mp4") as video:
            with patch.dict(sys.modules, {"googleapiclient.http": media_module}):
                response = upload_video.upload_video(
                    Service(),
                    Path(video.name),
                    {
                        "snippet": {"title": "Title"},
                        "status": {"privacyStatus": "private"},
                    },
                )

        self.assertEqual(response["id"], "video-id")
        self.assertEqual(calls["part"], "snippet,status")
        self.assertFalse(calls["notifySubscribers"])
        self.assertTrue(calls["media_arguments"][2])


if __name__ == "__main__":
    unittest.main()
