from unittest.mock import MagicMock, patch
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_accessible(
    mock_valid_url: MagicMock, mock_internet: MagicMock
) -> None:
    # Caso 1: Ambas verdaderas -> Debe retornar "Accessible"
    mock_internet.return_value = True
    mock_valid_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_cannot_access_if_only_connection(
    mock_valid_url: MagicMock, mock_internet: MagicMock
) -> None:
    # Caso 2: Solo internet True, URL False -> Debe retornar "Not accessible"
    mock_internet.return_value = True
    mock_valid_url.return_value = False
    assert (
        can_access_google_page("https://url-invalida.com")
        == "Not accessible"
    )


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_cannot_access_if_only_valid_url(
    mock_valid_url: MagicMock, mock_internet: MagicMock
) -> None:
    # Caso 3: Internet False, URL True -> Debe retornar "Not accessible"
    mock_internet.return_value = False
    mock_valid_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_neither(
    mock_valid_url: MagicMock, mock_internet: MagicMock
) -> None:
    # Caso 4: Ambas falsas -> Debe retornar "Not accessible"
    mock_internet.return_value = False
    mock_valid_url.return_value = False
    assert (
        can_access_google_page("https://url-invalida.com")
        == "Not accessible"
    )
