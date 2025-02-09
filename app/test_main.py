import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_valid_url_return, mock_internet_return, expected",
    [
        (True, True, "Accessible"),  # Коректний URL + є інтернет → Accessible
        (True, False, "Not accessible"),  # Коректний URL, але немає інтернету
        (False, True, "Not accessible"),  # Невірний URL, є інтернет
        (False, False, "Not accessible"),  # Невірний URL і немає інтернету
    ],
)
@patch("app.main.has_internet_connection")  # Мокаємо has_internet_connection
@patch("app.main.valid_google_url")  # Мокаємо valid_google_url
def test_can_access_google_page(
    mock_valid_url: patch,
    mock_internet: patch,
    mock_valid_url_return: bool,
    mock_internet_return: bool,
    expected: str,
) -> None:
    """Перевіряє, чи can_access_google_page повертає правильний результат."""

    # Налаштовуємо моки
    mock_valid_url.return_value = mock_valid_url_return
    mock_internet.return_value = mock_internet_return

    # Викликаємо функцію
    result = can_access_google_page("https://www.google.com")

    # Перевіряємо результат
    assert result == expected

    # Переконуємося, що функції були викликані один раз
    mock_valid_url.assert_called_once_with("https://www.google.com")
    mock_internet.assert_called_once()
