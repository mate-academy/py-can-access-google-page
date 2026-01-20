from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_return_url_and_connection(mocked_url: mock,
                                          mocked_connection: mock) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = True
    assert can_access_google_page("good_url") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_return_not_url(mocked_url: mock,
                               mocked_connection: mock) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = True
    assert can_access_google_page("good_url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_return_not_connection(mocked_url: mock,
                                      mocked_connection: mock) -> None:
    mocked_url.return_value = True
    mocked_connection.return_value = False
    assert can_access_google_page("good_url") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_return_not_url_connection(mocked_url: mock,
                                          mocked_connection: mock) -> None:
    mocked_url.return_value = False
    mocked_connection.return_value = False
    assert can_access_google_page("good_url") == "Not accessible"
