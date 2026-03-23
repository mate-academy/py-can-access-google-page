from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_return_true_when_url_is_valid_and_connection_exists(
    mocked_valid_google_url: bool,
    mocked_has_internet_connection: bool,
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True

    result = can_access_google_page("https://google.com")

    assert result == "Accessible"