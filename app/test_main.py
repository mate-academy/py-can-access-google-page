from unittest.mock import MagicMock, patch
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet, is_valid_url, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock,
        has_internet: bool,
        is_valid_url: bool,
        expected_result: str,
) -> None:
    mock_has_internet_connection.return_value = has_internet
    mock_valid_google_url.return_value = is_valid_url

    assert can_access_google_page("https://www.google.com") == expected_result


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_short_circuit(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock,
) -> None:
    mock_has_internet_connection.return_value = False

    can_access_google_page("https://www.google.com")

    mock_valid_google_url.assert_not_called()
