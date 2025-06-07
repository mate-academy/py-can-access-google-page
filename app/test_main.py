from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_access_google_page_pass(mock_internet: MagicMock,
                                 mock_valid_url: MagicMock) -> None:
    url = "https://www.google.com"
    assert can_access_google_page(url=url) == "Accessible"
    mock_valid_url.assert_called_once_with(url)
    mock_internet.assert_called_once()


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_access_google_page_with_no_internet(
        mocked_internet: MagicMock, mocked_valid_url: MagicMock) -> None:
    url = "https://www.google.com"
    assert can_access_google_page(url=url) == "Not accessible"
    mocked_valid_url.assert_called_once_with(url=url)
    mocked_internet.assert_called_once()


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_access_google_page_with_false_url(
        mocked_internet: MagicMock, mocked_valid_url: MagicMock) -> None:
    url = "https://www.google.com"
    assert can_access_google_page(url=url) == "Not accessible"
    mocked_valid_url.assert_called_once_with(url)
    mocked_internet.assert_called_once()
