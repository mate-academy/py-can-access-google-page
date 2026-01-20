from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, connection, expected_result",
    [
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible"),
    ],
    ids=[
        "'Not accessible' if invalid url and doesn't have connection",
        "'Not accessible' if valid url and doesn't have connection",
        "'Not accessible' if invalid url and have connection",
        "'Accessible' if valid url and connection",
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_valid_url: bool,
    mock_connection: bool,
    valid_url: bool,
    connection: bool,
    expected_result: str,
) -> None:
    mock_valid_url.return_value = valid_url
    mock_connection.return_value = connection
    assert can_access_google_page("https://www.google.com") == expected_result
