import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize("url_return, internet_return, expected", [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible"),
])
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_url: bool,
    mock_internet: bool,
    url_return: bool,
    internet_return: bool,
    expected: str,
) -> None :
    mock_url.return_value = url_return
    mock_internet.return_value = internet_return
    assert can_access_google_page("https://www.google.com") == expected
