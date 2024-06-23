from unittest import mock
from app.main import valid_google_url, has_internet_connection


def mock_valid_google_url(url: str, status_code: int) -> bool:
    with mock.patch("requests.get") as mock_requests_get:
        mock_response = mock_requests_get.return_value
        mock_response.status_code = status_code
        return valid_google_url(url)


def mock_has_internet_connection(hour: int) -> bool:
    with mock.patch("datetime.datetime") as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.hour = hour
        return has_internet_connection()


def test_can_access_google_page() -> None:
    assert mock_valid_google_url("https://www.google.com", 200) is True
    assert mock_has_internet_connection(10) is True


def test_can_access_google_page_wrong_time() -> None:
    assert mock_valid_google_url("https://www.google.com", 200) is True
    assert mock_has_internet_connection(2) is False


def test_can_access_google_page_wrong_url() -> None:
    assert mock_valid_google_url("https://www.google.com", 404) is False
    assert mock_has_internet_connection(10) is True
