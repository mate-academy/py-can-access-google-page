from app.main import can_access_google_page

from unittest import mock


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url_and_no_internet(
        mock_valid_url: mock,
        mock_internet_connection: mock
) -> None:
    mock_valid_url.return_value = False
    mock_internet_connection.return_value = False
    assert can_access_google_page("https://www.google") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_invalid_url(
        mock_valid_url: mock,
        mock_internet_connection: mock
) -> None:
    mock_valid_url.return_value = False
    mock_internet_connection.return_value = True
    assert can_access_google_page("https://www.google") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_no_internet(
        mock_valid_url: mock,
        mock_internet_connection: mock
) -> None:
    mock_valid_url.return_value = True
    mock_internet_connection.return_value = False
    assert can_access_google_page(
        "https://www.google.com/"
    ) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access(
        mock_valid_url: mock,
        mock_internet_connection: mock
) -> None:
    mock_valid_url.return_value = True
    mock_internet_connection.return_value = True
    assert can_access_google_page("https://www.google.com/") == "Accessible"
