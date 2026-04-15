import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_status, internet_status, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: bool,
        mock_has_internet_connection: bool,
        url_status: bool ,
        internet_status: bool,
        expected: str
) -> None:
    mock_valid_google_url.return_value = url_status
    mock_has_internet_connection.return_value = internet_status

    assert can_access_google_page("https://www.google.com") == expected
