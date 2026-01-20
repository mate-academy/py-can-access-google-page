from unittest.mock import patch, Mock

from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_accessible(
        valid_mock: Mock,
        connection_mock: Mock
) -> None:
    valid_mock.return_value = True
    connection_mock.return_value = True

    assert can_access_google_page("http://google.com") == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_should_return_not_accessible_if_not_valid_google_url(
        valid_mock: Mock,
        connection_mock: Mock
) -> None:
    valid_mock.return_value = True
    connection_mock.return_value = False

    assert can_access_google_page("http://google.com") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_should_return_not_accessible_if_not_internet_connection(
        valid_mock: Mock,
        connection_mock: Mock
) -> None:
    valid_mock.return_value = False
    connection_mock.return_value = True

    assert can_access_google_page("http://google.com") == "Not accessible"
