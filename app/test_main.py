from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mock_internet: type[mock],
        mock_url: type[mock]
) -> None:
    mock_internet.return_value = True
    mock_url.return_value = True

    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url_and_connection_not_exists(
        mock_internet: type[mock],
        mock_url: type[mock]
) -> None:
    mock_internet.return_value = False
    mock_url.return_value = False

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_not_exist(
        mock_internet: type[mock],
        mock_url: type[mock]
) -> None:
    mock_internet.return_value = False
    mock_url.return_value = True

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url_and_connection_exist(
        mock_internet: type[mock],
        mock_url: type[mock]
) -> None:
    mock_internet.return_value = True
    mock_url.return_value = False

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
