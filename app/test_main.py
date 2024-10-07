import pytest
from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, has_internet_connection, valid_google_url, can_access",
    [
        pytest.param(
            "https://www.google.com/", True, True, "Accessible",
            id="Accessible if have internet connection and valid url"
        ),
        pytest.param(
            "https://www.google.com", False, True, "Not accessible",
            id="Not accessible if no internet connection"
        ),
        pytest.param(
            "https://www.youtube.com", True, False, "Not accessible",
            id="Not accessible if no valid google url"
        )
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_url: MagicMock,
        mock_has_internet: MagicMock,
        url: str,
        has_internet_connection: bool,
        valid_google_url: bool,
        can_access: str
) -> None:
    mock_has_internet.return_value = has_internet_connection
    mock_valid_url.return_value = valid_google_url

    assert can_access_google_page(url) == can_access
