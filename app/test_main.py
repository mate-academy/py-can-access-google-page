from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_accessible(mocked_url: bool, mocked_connection: bool) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("http:") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_not_accessible_only_url(mocked_url: bool,
                                     mocked_connection: bool) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page("http:") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_url_not_accessible_only_connection(mocked_url: bool,
                                            mocked_connection: bool) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page("http:") == "Not accessible"
