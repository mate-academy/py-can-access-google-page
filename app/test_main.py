import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_connection, expected",
    [
        (True, True, "Accessible"),       # ✅ URL válida + internet disponível
        (True, False, "Not accessible"),  # ❌ só URL válida
        (False, True, "Not accessible"),  # ❌ só internet disponível
        (False, False, "Not accessible"), # ❌ nenhum dos dois
    ],
)
def test_can_access_google_page(valid_url, has_connection, expected):
    # Simulando funções auxiliares
    with patch("app.main.valid_google_url", return_value=valid_url):
        with patch("app.main.has_internet_connection", return_value=has_connection):
            result = can_access_google_page("http://fake-url.com")
            assert result == expected
