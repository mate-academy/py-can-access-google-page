from unittest.mock import patch

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_valid_google_page_has_connection(
    mock_internet: callable,
    mock_valid_url: callable
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cant_access_invalid_google_page_has_connection(
    mock_internet: callable,
    mock_valid_url: callable
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True

    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cant_access_valid_google_page_no_connection(
    mock_internet: callable,
    mock_valid_url: callable
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cant_access_invalid_google_page_no_connection(
    mock_internet: callable,
    mock_valid_url: callable
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"
