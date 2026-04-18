from collections.abc import Callable
from unittest import mock


from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page(mock_valid: Callable,
                                mock_internet: Callable) -> None:
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_invalid_google_url(mock_valid: Callable,
                            mock_internet: Callable) -> None:
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_cannot_access_google_page(mock_valid: Callable,
                                   mock_internet: Callable) -> None:
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"
