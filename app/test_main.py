from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_success(mocked_internet_connection: None,
                 mocked_valid_url: str) -> None:
    mocked_internet_connection.return_value = True
    mocked_valid_url.return_value = True

    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_invalid_url(mocked_internet_connection: None,
                     mocked_valid_url: str) -> None:
    mocked_internet_connection.return_value = True
    mocked_valid_url.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_invalid_time(mocked_internet_connection: None,
                      mocked_valid_url: str) -> None:
    mocked_internet_connection.return_value = False
    mocked_valid_url.return_value = True

    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_invalid_time_and_url(mocked_internet_connection: None,
                              mocked_valid_url: str) -> None:
    mocked_internet_connection.return_value = False
    mocked_valid_url.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"
