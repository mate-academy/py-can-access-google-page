from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_valid_google_url: MagicMock,
                                mocked_has_internet_connection: MagicMock
                                ) -> None:
    assert can_access_google_page("url") == "Accessible"
    mocked_has_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once()


@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_no_connection(
        mocked_has_internet_connection: MagicMock
) -> None:
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
def test_not_accessible_when_invalid_url(
        mocked_valid_google_url: MagicMock) -> None:
    mocked_valid_google_url.return_value = False
    assert can_access_google_page("url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_no_connection_and_invalid_url(
        mocked_valid_google_url: MagicMock,
        mocked_has_internet_connection: MagicMock) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("url") == "Not accessible"
