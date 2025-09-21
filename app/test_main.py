# app/test_main.py
from unittest.mock import Mock
from _pytest.monkeypatch import MonkeyPatch
import pytest

from app.main import can_access_google_page


def test_accessible_when_valid_url_and_internet(
    monkeypatch: MonkeyPatch,
) -> None:
    """Return 'Accessible' quando URL é válida e há internet."""
    url = "https://any.google.url/"

    mock_valid = Mock(return_value=True)
    mock_internet = Mock(return_value=True)

    # Patch exatamente onde as funções são usadas
    monkeypatch.setattr("app.main.valid_google_url", mock_valid)
    monkeypatch.setattr("app.main.has_internet_connection", mock_internet)

    assert can_access_google_page(url) == "Accessible"

    mock_valid.assert_called_once_with(url)
    mock_internet.assert_called_once_with()


@pytest.mark.parametrize(
    "is_valid, has_net",
    [
        (True, False),
        (False, True),
        (False, False),
    ],
)
def test_not_accessible_if_any_condition_is_false(
    monkeypatch: MonkeyPatch, is_valid: bool, has_net: bool
) -> None:
    """
    Deve retornar 'Not accessible' quando qualquer condição falhar.
    Se não há internet, a função pode curto-circuitar e nem verificar a URL.
    """
    url = "https://whatever"

    mock_valid = Mock(return_value=is_valid)
    mock_internet = Mock(return_value=has_net)

    monkeypatch.setattr("app.main.valid_google_url", mock_valid)
    monkeypatch.setattr("app.main.has_internet_connection", mock_internet)

    assert can_access_google_page(url) == "Not accessible"

    # Sempre deve checar conectividade
    mock_internet.assert_called_once_with()

    # Só valida a URL se houver internet disponível
    if has_net:
        mock_valid.assert_called_once_with(url)
    else:
        assert mock_valid.call_count == 0
