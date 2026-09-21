from unittest.mock import MagicMock, patch

from app import main


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_accessible(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock,
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True

    assert main.can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_url_without_internet(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock,
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False

    assert (
        main.can_access_google_page("https://google.com")
        == "Not accessible"
    )


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_with_internet(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock,
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True

    assert (
        main.can_access_google_page("https://example.com")
        == "Not accessible"
    )


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_without_internet(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock,
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = False

    assert (
        main.can_access_google_page("https://example.com")
        == "Not accessible"
    )
