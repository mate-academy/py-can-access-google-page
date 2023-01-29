from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid: str,
        mocked_connection: str
) -> None:
    mocked_valid.return_value = True
    mocked_connection.return_value = True

    assert can_access_google_page("url") == "Accessible"

    mocked_valid.return_value = True
    mocked_connection.return_value = False

    assert can_access_google_page("url") == "Not accessible"

    mocked_valid.return_value = False
    mocked_connection.return_value = True

    assert can_access_google_page("url") == "Not accessible"

    mocked_valid.return_value = False
    mocked_connection.return_value = False

    assert can_access_google_page("url") == "Not accessible"
