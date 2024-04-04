import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page
from freezegun import freeze_time


@pytest.fixture
def mock_valid_google_url() -> MagicMock:
    with patch("app.main.requests.get") as mock_get:
        yield mock_get


def test_accessibility_with_valid_connection(
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value.status_code = 200

    with freeze_time("2024-04-04 10:00:00"):
        result = can_access_google_page("https://www.google.com")
        assert result == "Accessible"


def test_cannot_access_if_only_valid_url(
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value.status_code = 404

    with freeze_time("2024-04-04 10:00:00"):
        result = can_access_google_page("https://www.invalidurl.com")
        assert result == "Not accessible"


def test_cannot_access_if_only_connection(
        mock_valid_google_url: MagicMock
) -> None:
    mock_valid_google_url.return_value.status_code = 200

    with freeze_time("2024-04-04 23:00:00"):
        result = can_access_google_page("https://www.google.com")
        assert result == "Not accessible"
