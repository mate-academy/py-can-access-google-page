from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_everything_is_fine(
        mocked_connection: MagicMock, mocked_valid_url: MagicMock
) -> None:
    mocked_valid_url.return_value = True
    mocked_connection.return_value = True

    result = can_access_google_page("https://google.com")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_no_connection(
        mocked_connection: MagicMock, mocked_valid_url: MagicMock
) -> None:
    mocked_valid_url.return_value = True
    mocked_connection.return_value = False

    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_valid_url_and_no_connection(
        mocked_connection: MagicMock, mocked_valid_url: MagicMock
) -> None:
    mocked_valid_url.return_value = False
    mocked_connection.return_value = False

    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_valid_url_and_fine_connection(
        mocked_connection: MagicMock, mocked_valid_url: MagicMock
) -> None:
    mocked_valid_url.return_value = False
    mocked_connection.return_value = True

    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"
