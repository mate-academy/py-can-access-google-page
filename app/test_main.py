import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url,internet_connection,access_google_page",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_check_access_page(
        mock_valid_google_url: bool,
        mock_has_internet_connection: bool,
        is_valid_url: bool,
        internet_connection: bool,
        access_google_page: str) -> None:
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = is_valid_url
    assert (can_access_google_page("") == access_google_page)
