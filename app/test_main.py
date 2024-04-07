import requests

from unittest import TestCase
from unittest.mock import patch


class TestGoogle(TestCase):
    def setUp(self) -> None:
        self.url = "https://www.google.com"

    def test_can_access_google_access(self) -> None:
        with patch(
                "app.main.has_internet_connection",
                return_value=True
        ):
            with patch(
                    "app.main.valid_google_url",
                    return_value=True
            ):
                with patch(
                        "app.main.can_access_google_page",
                        return_value=True
                ):
                    response = requests.get(self.url)
                    self.assertEqual(response.status_code, 200)
