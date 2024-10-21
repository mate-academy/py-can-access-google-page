from unittest.mock import patch
from app.main import can_access_google_page


def mock_functions(valid_url: bool, has_internet: bool):
    patch("app.main.valid_google_url", return_value=valid_url).start()
    patch("app.main.has_internet_connection", return_value=has_internet).start()


def test_accessible_page() -> None:
    mock_functions(valid_url=True, has_internet=True)

    result = can_access_google_page("url")
    assert result == "Accessible"


def test_not_accessible_due_to_invalid_url() -> None:
    mock_functions(valid_url=False, has_internet=True)

    result = can_access_google_page("url")
    assert result == "Not accessible"


def test_not_accessible_due_to_no_internet() -> None:
    mock_functions(valid_url=True, has_internet=False)

    result = can_access_google_page("url")
    assert result == "Not accessible"
