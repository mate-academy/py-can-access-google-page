from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_should_return_accessible_if_url_valid_and_internet_available(
    mock_internet, mock_url
) -> None:
    mock_internet.return_value = True
    mock_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_should_return_not_accessible_if_url_invalid(
    mock_internet, mock_url
) -> None:
    mock_internet.return_value = True
    mock_url.return_value = False
    assert can_access_google_page("https://fake.google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_should_return_not_accessible_if_no_internet(
    mock_internet, mock_url
) -> None:
    mock_internet.return_value = False
    mock_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_should_return_not_accessible_if_no_internet_and_invalid_url(
    mock_internet, mock_url
) -> None:
    mock_internet.return_value = False
    mock_url.return_value = False
    assert can_access_google_page("https://bad.google.com") == "Not accessible"
