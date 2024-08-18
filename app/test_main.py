from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mocked_connection: callable,
        mocked_validation: callable
) -> None:

    url = "https://google.com"

    mocked_connection.return_value = True
    mocked_validation.return_value = True
    assert can_access_google_page(url) == "Accessible"

    mocked_connection.return_value = False
    mocked_validation.return_value = True
    assert can_access_google_page(url) == "Not accessible"

    mocked_connection.assert_called()
    mocked_validation.assert_called_with(url)
