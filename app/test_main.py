from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page(mock_valid_url: mock.MagicMock,
                                mock_internet: mock.MagicMock) -> None:
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_should_check_function_was_called(mocked_url: mock.MagicMock,
                                          mocked_connection:
                                          mock.MagicMock) -> None:
    can_access_google_page("https://www.google.com")
    mocked_url.assert_called_once()
    mocked_connection.assert_called_once()


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_cant_access_google_page(mock_valid_url: mock.MagicMock,
                                 mock_internet: mock.MagicMock) -> None:
    url = "https://www.non.google.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_if_no_internet_connection(mock_valid_url: mock.MagicMock,
                                   mock_internet: mock.MagicMock) -> None:
    url = "https://www.non.google.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_if_not_valid_url(mock_valid_url: mock.MagicMock,
                          mock_internet: mock.MagicMock) -> None:
    url = "https://www.non.google.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"
