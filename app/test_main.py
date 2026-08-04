from unittest.mock import MagicMock, patch
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, has_internet, expected_result",
    [
        pytest.param(True, True, "Accessible", id="valid_url_and_has_internet"),
        pytest.param(True, False, "Not accessible", id="valid_url_but_no_internet"),
        pytest.param(False, True, "Not accessible", id="invalid_url_but_has_internet"),
        pytest.param(False, False, "Not accessible", id="invalid_url_and_no_internet"),
    ],
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_url: MagicMock,
    mock_has_internet: MagicMock,
    is_valid_url: bool,
    has_internet: bool,
    expected_result: str,
) -> None:
    mock_valid_url.return_value = is_valid_url
    mock_has_internet.return_value = has_internet

    url = "https://www.google.com"
    assert can_access_google_page(url) == expected_result
