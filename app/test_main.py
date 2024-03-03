from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_valid_url_and_connection_exists(
    mocked_has_internet_connection: mock.Mock,
    mocked_valid_google_url: mock.Mock
) -> None:
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_valid_url_and_no_connection_exists(
    mocked_has_internet_connection: mock.Mock,
    mocked_valid_google_url: mock.Mock
) -> None:
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_no_valid_url_and_connection_exists(
    mocked_has_internet_connection: mock.Mock,
    mocked_valid_google_url: mock.Mock
) -> None:
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
