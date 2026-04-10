from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    # Caso 1: URL válida y hay conexión a internet
    with patch("app.main.valid_google_url") as mock_url, \
         patch("app.main.has_internet_connection") as mock_internet:

        mock_url.return_value = True
        mock_internet.return_value = True

        result = can_access_google_page("https://google.com")
        assert result == "Accessible"


def test_can_access_google_page_invalid_url() -> None:
    # Caso 2: URL inválida aunque haya internet
    with patch("app.main.valid_google_url") as mock_url, \
         patch("app.main.has_internet_connection") as mock_internet:

        mock_url.return_value = False
        mock_internet.return_value = True

        result = can_access_google_page("https://not-google.com")
        assert result == "Not accessible"


def test_can_access_google_page_no_internet() -> None:
    # Caso 3: URL válida pero no hay conexión (fuera de horario)
    with patch("app.main.valid_google_url") as mock_url, \
         patch("app.main.has_internet_connection") as mock_internet:

        mock_url.return_value = True
        mock_internet.return_value = False

        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"
