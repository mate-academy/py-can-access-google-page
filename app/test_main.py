from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_function_has_been_called(
    mocked_valid_google_url: MagicMock,
    mocked_has_internet_connection: MagicMock,
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    result = can_access_google_page("url")
    assert result == "Accessible"

    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True
    result = can_access_google_page("url")
    assert result == "Not accessible"

    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    result = can_access_google_page("url")
    assert result == "Not accessible"

    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    result = can_access_google_page("url")
    assert result == "Not accessible"
