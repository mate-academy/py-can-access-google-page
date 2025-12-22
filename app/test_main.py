import pytest
from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize("valid_url, connection, expected",
                         [
                             (True, True, "Accessible"),
                             (False, True, "Not accessible"),
                             (True, False, "Not accessible"),
                         ])
def test_valid_url_and_connection_exists(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock,
        valid_url: bool,
        connection: bool,
        expected: str
) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_has_internet_connection.return_value = connection
    response = can_access_google_page("https://www.google.com")
    if mocked_has_internet_connection.return_value:
        (mocked_valid_google_url
         .assert_called_with("https://www.google.com"))
    else:
        mocked_valid_google_url.assert_not_called()
    assert response == expected
