import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet_connection, access_status",
    [
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_page(
        mock_valid_url: bool,
        mock_has_internet: bool,
        url: bool,
        internet_connection: bool,
        access_status: str
) -> None:
    mock_valid_url.return_value = url
    mock_has_internet.return_value = internet_connection

    result = can_access_google_page("https://www.google.com/")

    assert result == access_status
