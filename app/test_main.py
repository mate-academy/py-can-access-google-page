import pytest
from unittest.mock import patch

import app.main as main


def test_accessible_when_internet_and_valid_url() -> None:
    """Powinno zwrócić 'Accessible', gdy jest internet i URL jest poprawny."""
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=True):
        assert main.can_access_google_page("https://www.google."
                                           "com") == "Accessible"


@pytest.mark.parametrize(
    "internet_ok,url_ok",
    [
        (False, True),
        (True, False),
        (False, False),
    ],
)
def test_not_accessible_when_any_condition_fails(
    internet_ok: bool,
    url_ok: bool,
) -> None:
    with patch("app.main.has_internet_connection", return_value=internet_ok), \
         patch("app.main.valid_google_url", return_value=url_ok):
        assert main.can_access_google_page("https://www.google."
                                           "com") == "Not accessible"
