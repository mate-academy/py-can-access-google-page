from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_if_connection_and_url_is_valid(mocked_url: str,
                                        mocked_connection: str) -> None:
    mocked_connection.return_value = True
    mocked_url.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_if_connection_and_url_is_invalid(mocked_url: str,
                                          mocked_connection: str) -> None:
    mocked_connection.return_value = False
    mocked_url.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_if_only_connection_is_valid(mocked_url: str,
                                     mocked_connection: str) -> None:
    mocked_connection.return_value = True
    mocked_url.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_if_only_url_is_valid(mocked_url: str,
                              mocked_connection: str) -> None:
    mocked_connection.return_value = False
    mocked_url.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"
