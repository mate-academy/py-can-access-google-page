from unittest.mock import patch

from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_success(
    mock_valid_url: object,
    mock_has_internet: object,
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True

    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_cannot_access_if_only_valid_url(
    mock_valid_url: object,
    mock_has_internet: object,
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_cannot_access_if_only_connection(
    mock_valid_url: object,
    mock_has_internet: object,
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    assert can_access_google_page("invalid-url") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_cannot_access_if_neither(
    mock_valid_url: object,
    mock_has_internet: object,
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = False

    assert can_access_google_page("invalid-url") == "Not accessible"
