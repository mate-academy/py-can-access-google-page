from unittest.mock import MagicMock
from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_access_google_with_success(mocked_connection: MagicMock,
                                    mocked_url: MagicMock) -> None:
    mocked_connection.return_value = True
    mocked_url.return_value = True

    assert can_access_google_page("http://ggo") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_access_google_with_wrong_url(mocked_connection: MagicMock,
                                      mocked_url: MagicMock) -> None:
    mocked_connection.return_value = True
    mocked_url.return_value = False

    assert can_access_google_page("http://ggo") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_access_google_with_wrong_time(mocked_connection: MagicMock,
                                       mocked_url: MagicMock) -> None:
    mocked_connection.return_value = False
    mocked_url.return_value = True

    assert can_access_google_page("http://ggo") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_access_google_with_all_wrong(mocked_connection: MagicMock,
                                      mocked_url: MagicMock) -> None:
    mocked_connection.return_value = False
    mocked_url.return_value = False

    assert can_access_google_page("http://ggo") == "Not accessible"
