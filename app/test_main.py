from unittest import TestCase, mock, main
from app.main import can_access_google_page


class TestCanAccessGooglePage(TestCase):
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_return_accessible(
            self,
            valid_google_url: mock.MagicMock,
            has_internet_connection: mock.MagicMock
    ) -> None:
        valid_google_url.return_value = True
        has_internet_connection.return_value = True
        self.assertEqual(can_access_google_page(""), "Accessible")

    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_false_in_internet_connection(
            self,
            valid_google_url: mock.MagicMock,
            has_internet_connection: mock.MagicMock
    ) -> None:
        valid_google_url.return_value = True
        has_internet_connection.return_value = False
        self.assertEqual(can_access_google_page(""), "Not accessible")

    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_false_in_valid_google_url(
            self,
            valid_google_url: mock.MagicMock,
            has_internet_connection: mock.MagicMock
    ) -> None:
        valid_google_url.return_value = False
        has_internet_connection.return_value = True
        self.assertEqual(can_access_google_page(""), "Not accessible")

    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_false_in_internet_and_valid(
            self,
            valid_google_url: mock.MagicMock,
            has_internet_connection: mock.MagicMock
    ) -> None:
        valid_google_url.return_value = False
        has_internet_connection.return_value = False
        self.assertEqual(can_access_google_page(""), "Not accessible")


if __name__ == "__main__":
    main()
