from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url,has_internet,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mock_has_internet: bool,
        mock_valid_url: bool,
        is_valid_url: bool,
        has_internet: bool,
        result: str) -> None:
    mock_valid_url.return_value = is_valid_url
    mock_has_internet.return_value = has_internet

    assert can_access_google_page("https://www.google.com/") == result
