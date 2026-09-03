from unittest.mock import patch, MagicMock
import app.main as main


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_accessible_when_both_true(
    mock_connection: MagicMock, mock_valid_url: MagicMock
) -> None:
    mock_connection.return_value = True
    mock_valid_url.return_value = True
    assert main.can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_only_connection_true(
    mock_connection: MagicMock, mock_valid_url: MagicMock
) -> None:
    mock_connection.return_value = True
    mock_valid_url.return_value = False
    assert (
        main.can_access_google_page("https://google.com") == "Not accessible"
    )


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_only_valid_url_true(
    mock_connection: MagicMock, mock_valid_url: MagicMock
) -> None:
    mock_connection.return_value = False
    mock_valid_url.return_value = True
    assert (
        main.can_access_google_page("https://google.com") == "Not accessible"
    )


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_not_accessible_when_both_false(
    mock_connection: MagicMock, mock_valid_url: MagicMock
) -> None:
    mock_connection.return_value = False
    mock_valid_url.return_value = False
    assert (
        main.can_access_google_page("https://google.com") == "Not accessible"
    )
