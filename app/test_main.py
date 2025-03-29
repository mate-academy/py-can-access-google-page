# app/test_main.py
from unittest.mock import patch
from app.main import can_access_google_page


# Тестові випадки для функції can_access_google_page
def test_can_access_google_page_success() -> None:
    # Тест, коли обидві умови виконуються (доступно)
    with patch("app.main.valid_google_url") as mock_valid_url:
        with patch("app.main.has_internet_connection") as mock_internet:
            mock_valid_url.return_value = True
            mock_internet.return_value = True

            результат = can_access_google_page("https://www.google.com")
            assert результат == "Accessible"
            mock_valid_url.assert_called_once_with("https://www.google.com")
            mock_internet.assert_called_once()


def test_can_access_google_page_no_internet() -> None:
    # Тест, коли URL валідний, але немає інтернету
    with patch("app.main.valid_google_url") as mock_valid_url:
        with patch("app.main.has_internet_connection") as mock_internet:
            mock_valid_url.return_value = True
            mock_internet.return_value = False

            результат = can_access_google_page("https://www.google.com")
            assert результат == "Not accessible"
            mock_valid_url.assert_not_called()  # Оцінка короткого замикання
            mock_internet.assert_called_once()


def test_can_access_google_page_invalid_url() -> None:
    # Тест, коли URL невалідний, але є інтернет
    with patch("app.main.valid_google_url") as mock_valid_url:
        with patch("app.main.has_internet_connection") as mock_internet:
            mock_valid_url.return_value = False
            mock_internet.return_value = True

            результат = can_access_google_page("https://www.google.com")
            assert результат == "Not accessible"
            mock_valid_url.assert_called_once_with("https://www.google.com")
            mock_internet.assert_called_once()


def test_can_access_google_page_both_false() -> None:
    # Тест, коли обидві умови не виконуються
    with patch("app.main.valid_google_url") as mock_valid_url:
        with patch("app.main.has_internet_connection") as mock_internet:
            mock_valid_url.return_value = False
            mock_internet.return_value = False

            результат = can_access_google_page("https://www.google.com")
            assert результат == "Not accessible"
            mock_valid_url.assert_not_called()  # Оцінка короткого замикання
            mock_internet.assert_called_once()
