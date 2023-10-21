from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_internet_connection: callable,
        mock_page_url: callable
) -> None:
    mock_internet_connection.return_value = True
    mock_page_url.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_return_not_accessible_if_no_internet_connection(
        mock_internet_connection: callable,
        mock_page_url: callable
) -> None:
    mock_internet_connection.return_value = False
    mock_page_url.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_return_not_accessible_if_invalid_url(
        mock_internet_connection: callable,
        mock_page_url: callable
) -> None:
    mock_internet_connection.return_value = True
    mock_page_url.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"
