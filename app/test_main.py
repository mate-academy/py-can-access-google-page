from unittest.mock import patch
from app.main import can_access_google_page


# O patch deve apontar para onde as funções são CHAMADAS (no arquivo main)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_url: bool,
        mock_has_internet: bool
) -> None:
    # Cenário 1: Tudo OK -> Deve retornar "Accessible"
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True

    result = can_access_google_page("https://google.com")
    assert result == "Accessible"

    # Cenário 2: URL inválida -> Deve retornar "Not accessible"
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    result = can_access_google_page("https://invalid.com")
    assert result == "Not accessible"

    # Cenário 3: Sem internet -> Deve retornar "Not accessible"
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False

    result = can_access_google_page("https://google.com")
    assert result == "Not accessible"
