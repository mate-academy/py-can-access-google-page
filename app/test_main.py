import pytest

from unittest import mock

from app.main import can_access_google_page


def test_call_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_google_url:
        can_access_google_page("https://google.com")
        mock_google_url.assert_called_once_with("https://google.com")


def test_call_has_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        can_access_google_page("https://google.com")
        mock_connection.assert_called_once()


@pytest.mark.parametrize(
    "url,response_url,response_connection,expected",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://google.com", True, False, "Not accessible"),
        ("google.com", False, True, "Not accessible"),
        ("google.com", False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        url: str,
        response_url: bool,
        response_connection: bool,
        expected: str,
) -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        with mock.patch("app.main.has_internet_connection") as mock_connection:
            mock_connection.return_value = response_connection
            mock_valid_url.return_value = response_url
            assert can_access_google_page(url) == expected
