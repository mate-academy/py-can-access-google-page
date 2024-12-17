from unittest.mock import patch
from app.main import can_access_google_page


# Тест для випадку, коли URL дійсний і є інтернет-з'єднання
def test_valid_url_and_connection() -> None:
    with patch("app.main.valid_google_url", return_value=True):
        with patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page(
                "https://www.google.com"
            ) == "Accessible"


# Тест для випадку, коли URL недійсний, але інтернет-з'єднання є
def test_invalid_url_and_connection_exists() -> None:
    with patch("app.main.valid_google_url", return_value=False):
        with patch("app.main.has_internet_connection", return_value=True):
            assert can_access_google_page(
                "https://www.invalid.com"
            ) == "Not accessible"


# Тест для випадку, коли URL дійсний, але немає інтернет-з'єднання
def test_valid_url_and_no_connection() -> None:
    with patch("app.main.valid_google_url", return_value=True):
        with patch("app.main.has_internet_connection", return_value=False):
            assert can_access_google_page(
                "https://www.google.com"
            ) == "Not accessible"


# Тест для випадку, коли ні URL, ні інтернет-з'єднання недоступні
def test_invalid_url_and_no_connection() -> None:
    with patch("app.main.valid_google_url", return_value=False):
        with patch("app.main.has_internet_connection", return_value=False):
            assert can_access_google_page(
                "https://www.invalid.com"
            ) == "Not accessible"
