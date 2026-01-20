import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,connection,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_has_internet_connection: MagicMock,
                                mocked_valid_google_url: MagicMock,
                                valid_url: bool,
                                connection: bool,
                                expected: str) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_has_internet_connection.return_value = connection
    response = can_access_google_page("https://www.google.com")
    assert response == expected
