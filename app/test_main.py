import pytest

from app.main import can_access_google_page
from unittest import mock


@pytest.mark.parametrize(
    "valid_url, has_internet, current_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "Should be access google.com",
        "Should be no access because the internet is down",
        "Should be no access because the URL does not exist",
        "Should be no access because lose the internet and URL incorrect"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_page: callable,
        mock_has_internet_connection: callable,
        valid_url: bool,
        has_internet: bool,
        current_result: str
) -> None:
    mock_valid_google_page.return_value = valid_url
    mock_has_internet_connection.return_value = has_internet
    assert can_access_google_page("https://google.com") == current_result
