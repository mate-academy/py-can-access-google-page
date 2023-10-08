import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "connection_status, url_validation, expected_result",
    [
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (True, True, "Accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "no connection, valid url",
        "connection OK, invalid url",
        "connection OK, valid url",
        "no connection, invalid url"
    ])
def test_can_access_google_page(
        mocked_valid_google_url: MagicMock,
        mocked_has_internet_connection: MagicMock,
        connection_status: bool,
        url_validation: bool,
        expected_result: str
) -> None:
    mocked_has_internet_connection.return_value = connection_status
    mocked_valid_google_url.return_value = url_validation
    assert expected_result == can_access_google_page("https://www.google.com")
