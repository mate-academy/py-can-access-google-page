from unittest import mock
from unittest.mock import Mock
from app.main import can_access_google_page
import pytest


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "valid_value,connection_value,google_page,result",
    [
        (True, True, "https://www.google.com", "Accessible"),
        (False, True, "https://www.google.com", "Not accessible"),
        (True, False, "https://www.google.com", "Not accessible"),
        (False, False, "https://www.google.com", "Not accessible"),
    ])
def test_can_access(
        mocked_valid: Mock,
        mocked_connection: Mock,
        valid_value: bool,
        connection_value: bool,
        google_page: str,
        result: str
) -> None:
    mocked_valid.return_value = valid_value
    mocked_connection.return_value = connection_value
    assert can_access_google_page(google_page) == result
