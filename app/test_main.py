from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_valid_url_and_connection_exists(mocked_url: callable,
                                         mocked_internet: callable) -> None:
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_valid_url_but_no_connection(mocked_url: callable,
                                     mocked_internet: callable) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_invalid_url_and_no_connection(mocked_url: callable,
                                       mocked_internet: callable) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_google_page_invalid_connection(mocked_url: callable,
                                        mocked_internet: callable) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"
