import pytest

from app.main import can_access_google_page
from unittest.mock import patch, MagicMock


@pytest.fixture()
def url() -> str:
    return "https://Chubur/py-can-access-google-page"


@pytest.mark.parametrize(
    "has_internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_url_and_conection(mock_valid_google_url: MagicMock,
                           mock_has_internet_connection: MagicMock,
                           has_internet: bool,
                           valid_url: bool,
                           expected: str,
                           url: str) -> None:
    mock_valid_google_url.return_value = has_internet
    mock_has_internet_connection.return_value = valid_url
    assert can_access_google_page(url) == expected
