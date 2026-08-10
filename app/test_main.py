import pytest
from unittest.mock import patch
from app.main import can_access_google_page

@pytest.mark.parametrize(
    "url,is_valid,internet,expected",
    [
        ("https://www.google.com", True, True, "Accessible"),        # валідний урл + інтернет
        ("https://www.google.com", True, False, "Not accessible"),   # валідний урл без інтернету
        ("https://invalid.com", False, True, "Not accessible"),      # невалідний урл з інтернетом
        ("https://invalid.com", False, False, "Not accessible"),     # невалідний урл без інтернету
    ]
)
def test_can_access_google_page(url, is_valid, internet, expected):
    # Мокаємо залежні функції
    with patch("app.main.valid_google_url", return_value=is_valid), \
         patch("app.main.has_internet_connection", return_value=internet):
        result = can_access_google_page(url)
        assert result == expected
