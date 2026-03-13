from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_have_access(
    mocked_url: MagicMock, mocked_internet: MagicMock
) -> None:
    mocked_url.return_value = True
    mocked_internet.return_value = True

    assert can_access_google_page("google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_not_valid_url(
    mocked_url: MagicMock, mocked_internet: MagicMock
) -> None:
    mocked_url.return_value = False
    mocked_internet.return_value = True

    assert can_access_google_page("google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_no_internet(
    mocked_url: MagicMock, mocked_internet: MagicMock
) -> None:
    mocked_url.return_value = True
    mocked_internet.return_value = False

    assert can_access_google_page("google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_no_internet_not_valid_url(
    mocked_url: MagicMock, mocked_internet: MagicMock
) -> None:
    mocked_url.return_value = False
    mocked_internet.return_value = False

    assert can_access_google_page("google.com") == "Not accessible"
