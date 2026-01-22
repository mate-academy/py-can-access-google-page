import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url_mock, internet_mock, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://invalid-url.com", False, True, "Not accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://invalid-url.com", False, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_internet: patch,
    mock_valid_url: patch,
    url: str,
    valid_url_mock: bool,
    internet_mock: bool,
    expected: str
) -> None:
    mock_valid_url.return_value = valid_url_mock
    mock_internet.return_value = internet_mock

    result = can_access_google_page(url)
    assert result == expected, (f"Помилка при перевірці url={url}, "
                                f"отримано {result}")
