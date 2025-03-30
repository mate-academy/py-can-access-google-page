import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_valid_url, mock_internet_connection, expected", [
        pytest.param(True, True, "Accessible",
                     id="URL is valid, Internet connection is available"),
        pytest.param(False, True, "Not accessible",
                     id="URL is not valid, internet connection is available"),
        pytest.param(True, False, "Not accessible",
                     id="URL is valid, no internet connection "),
        pytest.param(False, False, "Not accessible",
                     id="URL is invalid, no internet connection")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_url: str,
        mock_internet: str,
        mock_valid_url: str,
        mock_internet_connection: str,
        expected: str
) -> None:
    mock_url.return_value = mock_valid_url
    mock_internet.return_value = mock_internet_connection

    result = can_access_google_page("http://www.google.com")
    assert result == expected
