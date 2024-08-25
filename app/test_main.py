from unittest import mock
from unittest.mock import Mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access(mocked_valid: Mock, mocked_connection: Mock) -> None:
    mocked_valid.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"

    mocked_valid.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"

    mocked_valid.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
