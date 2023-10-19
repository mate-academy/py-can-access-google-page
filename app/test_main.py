import pytest

from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, google_url, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool,
        internet_connection: bool,
        google_url: bool,
        result: str
) -> None:
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = google_url
    assert can_access_google_page("http://www.google.com") == result
