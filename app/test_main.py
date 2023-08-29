from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_if_has_connection_and_valid_url(
        mocked_valid_google_url,
        mocked_has_internet_connection
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True

    assert can_access_google_page("url") == "Accessible"

    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True

    assert can_access_google_page("url") == "Not accessible"

    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False

    assert can_access_google_page("url") == "Not accessible"

    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    assert can_access_google_page("url") == "Not accessible"
