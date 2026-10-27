from unittest import mock


from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_accessible(
    mock_valid_url: mock.MagicMock,
    mock_has_internet_connection: mock.MagicMock,
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_invalid_url(
    mock_valid_url: mock.MagicMock,
    mock_has_internet_connection: mock.MagicMock,
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_no_internet(
    mock_valid_url: mock.MagicMock,
    mock_has_internet_connection: mock.MagicMock,
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet_connection.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_neither(
    mock_valid_url: mock.MagicMock,
    mock_has_internet_connection: mock.MagicMock,
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet_connection.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"
