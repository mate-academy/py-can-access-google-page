import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.fixture
def mock_valid_google_url() -> "patch":
    with patch("app.main.valid_google_url") as mock:
        yield mock


@pytest.fixture
def mock_has_internet_connection() -> "patch":
    with patch("app.main.has_internet_connection") as mock:
        yield mock


@pytest.mark.parametrize("url, valid_url, has_internet, expected_result", [
    ("http://www.google.com", True, True, "Accessible"),
    ("http://invalidurl", False, True, "Not accessible"),
    ("http://www.google.com", True, False, "Not accessible"),
])
def test_can_access_google_page(
        mock_valid_google_url: "patch",
        mock_has_internet_connection: "patch",
        url: str,
        valid_url: bool,
        has_internet: bool,
        expected_result: str
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_internet

    result = can_access_google_page(url)

    assert result == expected_result
