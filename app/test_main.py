from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_can_access_google_when_all_true(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_can_not_access_google_when_connection_true_url_false(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    assert can_access_google_page("https://inval-url.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_can_not_access_google_when_connection_false_url_true(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_can_not_access_google_when_all_false(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    assert can_access_google_page("https://inval-url.com") == "Not accessible"
