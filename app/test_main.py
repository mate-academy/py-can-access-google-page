import pytest
from unittest.mock import Mock, patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, result",
    [
        ("https://mate.academy/", "Accessible"),
        ("https://invalid.link/hope", "Accessible")  # ?
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock,
        url: str,
        result: str
) -> None:
    assert can_access_google_page(url) == result
    mock_has_internet_connection.assert_called_once()
    mock_valid_google_url.assert_called_once()
