from unittest.mock import MagicMock, patch
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "simulation_url, simulation_internet, resultat_attendu",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_scenarios(
    mock_valid_url: MagicMock,
    mock_has_internet: MagicMock,
    simulation_url: bool,
    simulation_internet: bool,
    resultat_attendu: str
) -> None:
    """Valide les 4 cas limites d'accès à la page Google via des mocks."""
    # On configure les comportements simulés (Stubs)
    mock_valid_url.return_value = simulation_url
    mock_has_internet.return_value = simulation_internet

    # Appel de la fonction cible
    resultat = can_access_google_page("https://www.google.com/")

    # Assertion finale
    assert resultat == resultat_attendu
