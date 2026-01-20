from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_valid_url_and_connection_exists(mocked_connection: callable,
                                         mocked_url: callable) -> None:
    assert can_access_google_page("https://www.google.com/") == \
           "Accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_no_connection_exists(mocked_connection: callable,
                              mocked_url: callable) -> None:
    assert can_access_google_page("https://www.google.com/") == \
           "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_url_is_not_valid(mocked_connection: callable,
                          mocked_url: callable) -> None:
    assert can_access_google_page("https://www.google.com/") == \
           "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_url_is_not_valid_and_no_connection(mocked_connection: callable,
                                            mocked_url: callable) -> None:
    assert can_access_google_page("https://www.google.com/") == \
           "Not accessible"
