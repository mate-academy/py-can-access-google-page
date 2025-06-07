from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_access_google_page_pass(mock_internet: MagicMock,
                                 mock_valid_url: MagicMock) -> None:
    url = "www.google.com"
    assert can_access_google_page(url=url) == "Accessible"
    mock_internet.called_once()
    mock_valid_url.called_once_with(url)


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_access_google_page_with_no_internet(
        mocked_internet: MagicMock, mocked_valid_url: MagicMock) -> None:
    url = "www.google.com"
    assert can_access_google_page(url=url) == "Not accessible"
    mocked_internet.called_once()
    mocked_valid_url.called_once_with(url)


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_access_google_page_with_false_url(
        mocked_internet: MagicMock, mocked_valid_url: MagicMock) -> None:
    url = "www.googl.com"
    assert can_access_google_page(url=url) == "Not accessible"
    mocked_internet.called_once()
    mocked_valid_url.called_once_with(url)
