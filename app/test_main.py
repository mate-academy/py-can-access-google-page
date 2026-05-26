from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_success(mock_valid, mock_internet) -> None:
    mock_valid.return_value = True
    mock_internet.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"
    mock_valid.assert_called_once()
    mock_internet.assert_called_once()


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_fail(mock_valid, mock_internet) -> None:
    mock_valid.return_value = False
    mock_internet.return_value = True

    assert can_access_google_page("https://google.com") == "Not accessible"
    mock_valid.assert_called_once()
    mock_internet.assert_called_once()
