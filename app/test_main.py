from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize("url, expected_result", [
    ("https://www.google.com", "Accessible"),
    ("https://www.example.com", "Not accessible"),
    ("invalid_url", "Not accessible")
], ids=[
    "Access Google",
    "Access Example",
    "Invalid URL"
])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: mock.MagicMock,
        mock_valid_google_url: mock.MagicMock,
        url: str,
        expected_result: str
) -> None:
    if url != "https://www.google.com":
        mock_valid_google_url.return_value = False
    assert can_access_google_page(url) == expected_result


@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_invalid_google_url(
        mock_has_internet_connection: mock.MagicMock
) -> None:
    mock_has_internet_connection.return_value = True
    with mock.patch("app.main.valid_google_url") as mock_valid_google_url:
        mock_valid_google_url.return_value = False
        assert can_access_google_page("invalid_url") == "Not accessible"


def test_can_access_google_page_no_internet_connection() -> None:
    with (
        mock.patch("app.main.has_internet_connection")
        as mock_has_internet_connection
    ):
        mock_has_internet_connection.return_value = False
        assert can_access_google_page(
            "https://www.google.com"
        ) == "Not accessible"
