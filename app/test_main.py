from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mocked_google_url: mock,
                                mocked_internet_connection: mock) -> None:
    mocked_google_url.return_value = True
    mocked_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"
    mocked_internet_connection.return_value = False
    mocked_google_url.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"
