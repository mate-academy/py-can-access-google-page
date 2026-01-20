from unittest import mock
from unittest.mock import Mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, is_has_connection, res",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_two_funk(
        mocked_valid_google_url: Mock,
        mocked_has_internet_connection: Mock,
        is_valid_url: bool,
        is_has_connection: bool,
        res: str,
) -> None:
    mocked_valid_google_url.return_value = is_valid_url
    mocked_has_internet_connection.return_value = is_has_connection
    assert can_access_google_page("http://google.com") == res
