from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "value_connection, value_valid, result",
    [
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible")
    ], ids=["no connection & no valid", "only connection",
            "only valid", "connection & valid"]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
        mock_valid_url: object, mock_connection: object,
        value_connection: bool, value_valid: bool, result: str) -> None:
    mock_connection.return_value = value_connection
    mock_valid_url.return_value = value_valid
    assert can_access_google_page("url") == result
