import pytest

from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection_result,valid_google_url_result,result",
    [
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (True, True, "Accessible"),
    ],
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url: callable,
        mock_has_internet_connection: callable,
        has_internet_connection_result: bool,
        valid_google_url_result: bool,
        result: str) -> None:
    mock_valid_google_url.return_value = valid_google_url_result
    mock_has_internet_connection.return_value = has_internet_connection_result
    assert can_access_google_page("https://www.google.com") == result
