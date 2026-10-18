from unittest.mock import MagicMock, patch
import pytest

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "has_internet,is_valid_url,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    mock_has_internet: MagicMock,
    mock_valid_url: MagicMock,
    has_internet: bool,
    is_valid_url: bool,
    expected_result: str,
) -> None:
    mock_has_internet.return_value = has_internet
    mock_valid_url.return_value = is_valid_url

    assert can_access_google_page("https://google.com") == expected_result


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_valid_url_not_called_without_internet(
    mock_has_internet: MagicMock,
    mock_valid_url: MagicMock,
) -> None:
    mock_has_internet.return_value = False

    can_access_google_page("https://google.com")

    mock_valid_url.assert_not_called()
