# app/test_main.py
from unittest.mock import patch
from app.main import can_access_google_page


def test_can_access_google_page_with_valid_url_and_internet() -> None:
    # Тестує випадок, коли URL валідний і є інтернет
    with patch("app.main.valid_google_url") as mock_valid_url:
        with patch("app.main.has_internet_connection") as mock_internet:
            mock_valid_url.return_value = True
            mock_internet.return_value = True

            result = can_access_google_page("https://www.google.com")
            assert result == "Accessible"
            mock_valid_url.assert_called_once_with("https://www.google.com")
            mock_internet.assert_called_once()


def test_can_access_google_page_with_valid_url_but_no_internet() -> None:
    # Тестує випадок, коли URL валідний, але немає інтернету
    with patch("app.main.valid_google_url") as mock_valid_url:
        with patch("app.main.has_internet_connection") as mock_internet:
            mock_valid_url.return_value = True
            mock_internet.return_value = False

            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"
            mock_valid_url.assert_not_called()  # Оцінка короткого замикання
            mock_internet.assert_called_once()


def test_can_access_google_page_with_invalid_url_and_internet() -> None:
    # Тестує випадок, коли URL невалідний, але є інтернет
    with patch("app.main.valid_google_url") as mock_valid_url:
        with patch("app.main.has_internet_connection") as mock_internet:
            mock_valid_url.return_value = False
            mock_internet.return_value = True

            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"
            mock_valid_url.assert_called_once_with("https://www.google.com")
            mock_internet.assert_called_once()


def test_can_access_google_page_with_invalid_url_and_no_internet() -> None:
    # Тестує випадок, коли URL невалідний і немає інтернету
    with patch("app.main.valid_google_url") as mock_valid_url:
        with patch("app.main.has_internet_connection") as mock_internet:
            mock_valid_url.return_value = False
            mock_internet.return_value = False

            result = can_access_google_page("https://www.google.com")
            assert result == "Not accessible"
            mock_valid_url.assert_not_called()  # Оцінка короткого замикання
            mock_internet.assert_called_once()
