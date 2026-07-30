from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google_page_is_accessible_with_valid_url_and_connection(
        mock_has_internet_connection: mock.MagicMock,
        mock_valid_google_url: mock.MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google_page_is_not_accessible_with_invalid_url(
        mock_has_internet_connection: mock.MagicMock,
        mock_valid_google_url: mock.MagicMock
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google_page_is_not_accessible_without_connection(
        mock_has_internet_connection: mock.MagicMock,
        mock_valid_google_url: mock.MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"
