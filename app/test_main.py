from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mocked_connection: callable,
        mocked_validation: callable
) -> None:

    url = "https://google.com"
    check_options = [
        (True, True, "Accessible", "is connection and the URL is valid"),
        (False, True, "Not accessible", "no connection"),
        (True, False, "Not accessible", "url is not valid"),
        (False, False, "Not accessible", "no connection and url is not valid")
    ]
    for option in check_options:
        connection, valid_url, expected_can_access, message = option
        mocked_connection.return_value = connection
        mocked_validation.return_value = valid_url
        assert can_access_google_page(url) == expected_can_access, message

    mocked_connection.assert_called()
    mocked_validation.assert_called_with(url)
