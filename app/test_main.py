from app.main import can_access_google_page
from unittest.mock import patch, MagicMock


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_when_url_valid_and_has_connection(
    mock_valid_url: MagicMock,
    mock_has_internet: MagicMock,
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True

    inter = can_access_google_page("https://google.com")
    assert inter == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_when_url_invalid(
    mock_valid_url: MagicMock,
    mock_has_internet: MagicMock,
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    new_inter = can_access_google_page("https://google.com")
    assert new_inter == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_when_no_internet(
    mock_valid_url: MagicMock,
    mock_has_internet: MagicMock,
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False

    number = can_access_google_page("https://google.com")
    assert number == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_when_no_internet_and_url_invalid(
    mock_valid_url: MagicMock,
    mock_has_internet: MagicMock,
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = False

    new_number = can_access_google_page("https://google.com")
    assert new_number == "Not accessible"
