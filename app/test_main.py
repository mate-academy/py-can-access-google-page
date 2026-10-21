from unittest.mock import MagicMock, patch
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_status, url_status, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "internet_and_url_valid",
        "internet_valid_url_invalid",
        "internet_invalid_url_valid",
        "internet_and_url_invalid",
    ],
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_url: MagicMock,
    mock_internet: MagicMock,
    internet_status: bool,
    url_status: bool,
    expected: str,
) -> None:
    mock_internet.return_value = internet_status
    mock_valid_url.return_value = url_status

    result = can_access_google_page("https://www.google.com")
    assert result == expected


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=False)
def test_strict_failure_only_internet(
    mock_valid_url: MagicMock, mock_internet: MagicMock
) -> None:
    # Si solo hay internet pero la URL es inválida, debe fallar obligatoriamente
    assert can_access_google_page("invalid-url") == "Not accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=True)
def test_strict_failure_only_valid_url(
    mock_valid_url: MagicMock, mock_internet: MagicMock
) -> None:
    # Si la URL es válida pero no hay internet, debe fallar obligatoriamente
    assert can_access_google_page("https://www.google.com") == "Not accessible"


def test_can_access_google_page_returns_str() -> None:
    with patch("app.main.has_internet_connection", return_value=True), \
         patch("app.main.valid_google_url", return_value=True):
        result = can_access_google_page("https://www.google.com")
        assert isinstance(result, str)
