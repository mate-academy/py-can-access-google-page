from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_has_internet_connection: bool,
        mocked_valid_google_url: bool
) -> None:

    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True

    assert can_access_google_page("https://www.youtube.com") == "Accessible"

    mocked_has_internet_connection.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"

    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"
