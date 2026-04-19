from unittest.mock import patch, MagicMock
import app.main as main_module


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(
    mock_connection: MagicMock,
    mock_url: MagicMock,
) -> None:
    mock_connection.return_value = True
    mock_url.return_value = True
    result = main_module.can_access_google_page("https://google.com")
    assert result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_if_only_connection_is_true(
    mock_connection: MagicMock,
    mock_url: MagicMock,
) -> None:
    mock_connection.return_value = True
    mock_url.return_value = False
    result = main_module.can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_if_only_valid_url_is_true(
    mock_connection: MagicMock,
    mock_url: MagicMock,
) -> None:
    mock_connection.return_value = False
    mock_url.return_value = True
    result = main_module.can_access_google_page("https://google.com")
    assert result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_if_both_false(
    mock_connection: MagicMock,
    mock_url: MagicMock,
) -> None:
    mock_connection.return_value = False
    mock_url.return_value = False
    result = main_module.can_access_google_page("https://google.com")
    assert result == "Not accessible"
