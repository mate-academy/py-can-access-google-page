import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_internet, expected_result",
    [
        pytest.param(True, True, "Accessible", id="test_accessible"),
        pytest.param(False, True, "Not accessible", id="test_invalid_url"),
        pytest.param(True, False, "Not accessible", id="test_no_internet"),
    ],
)
def test_can_access_google_page(
    valid_url: bool,
    has_internet: bool,
    expected_result: str,
) -> None:
    with patch("app.main.valid_google_url", return_value=valid_url), patch(
        "app.main.has_internet_connection", return_value=has_internet
    ):
        result = can_access_google_page("https://www.google.com")
        assert result == expected_result
