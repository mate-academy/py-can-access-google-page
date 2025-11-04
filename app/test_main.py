from unittest import mock, TestCase
from unittest.mock import MagicMock
from app.main import valid_google_url
from app.main import has_internet_connection
from app.main import can_access_google_page


class TestValidGoogleUrl(TestCase):
    @mock.patch("app.main.requests.get")
    def test_should_request_with_correct_args(
            self,
            mock_request: MagicMock) -> None:
        valid_google_url("https://google.com")
        mock_request.assert_called_once_with("https://google.com")

    @mock.patch("app.main.requests.get")
    def test_should_return_true(
            self,
            mock_request: MagicMock) -> None:
        mock_request.return_value.status_code = 200
        assert valid_google_url("https://google.com") is True

    @mock.patch("app.main.requests.get")
    def test_should_return_false(
            self,
            mock_request: MagicMock) -> None:
        mock_request.return_value.status_code = 404
        assert valid_google_url("google.com") is False


class TestHasInternetConnection(TestCase):

    @mock.patch("app.main.datetime.datetime")
    def test_call_datetime_now(
            self,
            mock_datetime: MagicMock) -> None:
        mock_datetime.now.return_value.hour = 15
        has_internet_connection()
        mock_datetime.now.assert_called_once()

    @mock.patch("app.main.datetime.datetime")
    def test_should_return_true_when_hour_is_6(
            self,
            mock_datetime: MagicMock) -> None:
        mock_datetime.now().hour = 6
        assert has_internet_connection() is True

    @mock.patch("app.main.datetime.datetime")
    def test_should_return_true_when_hour_is_22(
            self,
            mock_datetime: MagicMock) -> None:
        mock_datetime.now().hour = 22
        assert has_internet_connection() is True

    @mock.patch("app.main.datetime.datetime")
    def test_should_return_false_when_hour_is_5(
            self,
            mock_datetime: MagicMock) -> None:
        mock_datetime.now().hour = 5
        assert has_internet_connection() is False

    @mock.patch("app.main.datetime.datetime")
    def test_should_return_false_when_hour_is_23(
            self,
            mock_datetime: MagicMock) -> None:
        mock_datetime.now().hour = 23
        assert has_internet_connection() is False


class TestCanAccessGooglePage(TestCase):
    def test_when_is_internet_connect_and_valid_url(self) -> None:
        with mock.patch("app.main.has_internet_connection") as mock_valid_url:
            with mock.patch("app.main.valid_google_url") as \
                    mock_internet_connect:
                mock_internet_connect.return_value = True
                mock_valid_url.return_value = True
                assert can_access_google_page("") == "Accessible"

    def test_when_url_is_not_valid(self) -> None:
        with mock.patch("app.main.has_internet_connection") as \
                mock_internet_connect:
            with mock.patch("app.main.valid_google_url") as \
                    mock_valid_url:
                mock_internet_connect.return_value = True
                mock_valid_url.return_value = False
                assert can_access_google_page("") == "Not accessible"

    def test_when_not_internet_connection(self) -> None:
        with mock.patch("app.main.has_internet_connection") as \
                mock_internet_connect:
            with mock.patch("app.main.valid_google_url") as \
                    mock_valid_url:
                mock_internet_connect.return_value = False
                mock_valid_url.return_value = True
                assert can_access_google_page("") == "Not accessible"

    def test_when_not_internet_connection_and_url_is_not_valid(self) -> None:
        with mock.patch("app.main.has_internet_connection") as \
                mock_internet_connect:
            with mock.patch("app.main.valid_google_url") as \
                    mock_valid_url:
                mock_internet_connect.return_value = False
                mock_valid_url.return_value = False

                assert can_access_google_page("") == "Not accessible"
