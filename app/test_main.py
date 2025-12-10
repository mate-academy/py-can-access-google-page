import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,is_valid_url,has_connection,expected_result",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://google.com", False, True, "Not accessible"),
        ("https://google.com", True, False, "Not accessible"),
        ("https://google.com", False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    url: str,
    is_valid_url: bool,
    has_connection: bool,
    expected_result: str
) -> None:
    with patch("app.main.valid_google_url") as mock_valid_url:
        with patch("app.main.has_internet_connection") as mock_has_connection:
            mock_valid_url.return_value = is_valid_url
            mock_has_connection.return_value = has_connection

            result = can_access_google_page(url)

            assert result == expected_result

            mock_has_connection.assert_called_once()

            if has_connection:
                mock_valid_url.assert_called_once_with(url)
            else:
                mock_valid_url.assert_not_called()
