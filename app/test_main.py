from unittest.mock import patch
import pytest
from app import main


@pytest.mark.parametrize(
    "valid_url, internet, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "valid_url_and_connection_exists",
        "valid_url_and_no_connection",
        "invalid_url_and_connection_exists",
        "invalid_url_and_no_connection",
    ],
)
def test_can_access_google_page(
        valid_url: bool,
        internet: bool,
        expected: str) -> None:
    with patch("app.main.valid_google_url") as mock_url:
        with patch("app.main.has_internet_connection") as mock_internet:
            mock_url.return_value = valid_url
            mock_internet.return_value = internet
            result = main.can_access_google_page("google.com")
            assert result == expected
            if internet:
                mock_url.assert_called_once_with("google.com")
            else:
                mock_url.assert_not_called()
            mock_internet.assert_called_once_with()
