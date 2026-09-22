from unittest.mock import MagicMock, patch
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "internet_connection,valid_url,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@pytest.mark.parametrize("url", ["https://google.com",
                                 "https://www.google.com"])
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_accessible(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
    internet_connection: bool,
    valid_url: bool,
    result: str,
    url: str
) -> None:
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = valid_url
    assert can_access_google_page(url) == result
