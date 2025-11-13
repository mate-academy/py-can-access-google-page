from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_when_can_access_google_page_and_internet(
        mocked_internet: mock.MagicMock,
        mocked_valid_url: mock.MagicMock
) -> None:
    mocked_internet.return_value = True
    mocked_valid_url.return_value = True
    url = "https://www.google.com"
    assert can_access_google_page(url) == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_when_cant_access_google_page_and_internet(
        mocked_internet: mock.MagicMock,
        mocked_valid_url: mock.MagicMock
) -> None:
    mocked_internet.return_value = False
    mocked_valid_url.return_value = False
    url = "https://www.google.com"
    assert can_access_google_page(url) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_when_cant_access_google_page(
        mocked_internet: mock.MagicMock,
        mocked_valid_url: mock.MagicMock
) -> None:
    mocked_internet.return_value = True
    mocked_valid_url.return_value = False
    url = "https://www.google.com"
    assert can_access_google_page(url) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_when_cant_access_internet(
        mocked_internet: mock.MagicMock,
        mocked_valid_url: mock.MagicMock
) -> None:
    mocked_internet.return_value = False
    mocked_valid_url.return_value = True
    url = "https://www.google.com"
    assert can_access_google_page(url) == "Not accessible"
