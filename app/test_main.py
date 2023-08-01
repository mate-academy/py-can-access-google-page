import pytest
from unittest.mock import patch
from app.main import can_access_google_page


def mock_valid_google_url(url: str) -> bool:
    return url.startswith("https://www.google.com")


def mock_has_internet_connection() -> bool:
    return True


def mock_no_internet_connection() -> bool:
    return False


@pytest.mark.parametrize("url, internet, expected_result",
                         [("https://www.google.com", True, "Accessible"),
                          ("https://www.google.com", False, "Not accessible"),
                          ("https://www.invdurl.com", True, "Not accessible")])
def test_can_access_google_page(
        url: str,
        internet: bool,
        expected_result: str
) -> None:
    with patch(
            "app.main.valid_google_url",
            side_effect=mock_valid_google_url
            if internet else lambda x: False):
        with patch("app.main.has_internet_connection", return_value=internet):
            result = can_access_google_page(url)
            assert result == expected_result
