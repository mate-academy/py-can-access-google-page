import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize("valid_url, internet_connection, result", [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible")
])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(
        mock_internet: bool,
        mock_url: bool,
        valid_url: bool,
        internet_connection: bool,
        result: str) -> None:
    mock_url.return_value = valid_url
    mock_internet.return_value = internet_connection
    assert can_access_google_page("url") == result
