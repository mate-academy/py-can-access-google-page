from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
# Success case
def test_can_access_google_page_success(
        mock_has_internet: mock.Mock,
        mock_valid_google_url: mock.Mock
) -> None:
    mock_has_internet.return_value = True
    mock_valid_google_url.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"
    mock_has_internet.assert_called_once()
    mock_valid_google_url.assert_called_once_with("https://www.google.com")


@mock.patch("app.main.has_internet_connection")
def test_failed_internet_connection(mock_has_internet: mock.Mock) -> None:
    mock_has_internet.return_value = False
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
    mock_has_internet.assert_called_once()


@mock.patch("app.main.valid_google_url")
def test_not_valid_url(mock_valid_google_url: mock.Mock) -> None:
    mock_valid_google_url.return_value = False
    result = can_access_google_page("https://ww.gogle.com")
    assert result == "Not accessible"
    mock_valid_google_url.assert_called_once_with("https://ww.gogle.com")
