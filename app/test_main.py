from unittest import TestCase, mock

from app.main import can_access_google_page


class TestCanAccessGooglePage(TestCase):
    def test_can_access_google_page_accessible(self) -> None:
        with mock.patch(
                "app.main.valid_google_url",
                return_value=True
        ):
            with mock.patch(
                    "app.main.has_internet_connection",
                    return_value=True
            ):
                self.assertEqual(
                    can_access_google_page("https://www.google.com"),
                    "Accessible"
                )

    def test_can_access_google_page_with_invalid_url(self) -> None:
        with mock.patch(
                "app.main.valid_google_url",
                return_value=False
        ):
            with mock.patch(
                    "app.main.has_internet_connection",
                    return_value=True
            ):
                self.assertEqual(
                    can_access_google_page("https://www.google.com"),
                    "Not accessible"
                )

    def test_can_access_google_page_with_no_internet(self) -> None:
        with mock.patch(
                "app.main.valid_google_url",
                return_value=True
        ):
            with mock.patch(
                    "app.main.has_internet_connection",
                    return_value=False
            ):
                self.assertEqual(
                    can_access_google_page("https://www.google.com"),
                    "Not accessible"
                )

    def test_can_access_google_page_with_no_internet_invalid_url(self) -> None:
        with mock.patch(
                "app.main.valid_google_url",
                return_value=False
        ):
            with mock.patch(
                    "app.main.has_internet_connection",
                    return_value=False
            ):
                self.assertEqual(
                    can_access_google_page("https://www.google.com"),
                    "Not accessible"
                )
