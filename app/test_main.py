from unittest.mock import patch
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet,is_valid_url,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    has_internet: bool,
    is_valid_url: bool,
    expected: str,
) -> None:
    with (
        patch("app.main.has_internet_connection") as mock_internet,
        patch("app.main.valid_google_url") as mock_url,
    ):
        mock_internet.return_value = has_internet
        mock_url.return_value = is_valid_url

        assert can_access_google_page("https://google.com") == expected
