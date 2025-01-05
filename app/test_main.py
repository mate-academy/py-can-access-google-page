import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "initial_value, value_to_add, expected_value",
    [
        pytest.param(True, True, "Accessible",
                     id="Internet accessible and URL right"),
        pytest.param(False, True, "Not accessible",
                     id="Internet is not accessible"),
        pytest.param(True, False, "Not accessible",
                     id="URL is not valid"),
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_internet: str,
    mock_valid_url: str,
    initial_value: str,
    value_to_add: str,
    expected_value: str
) -> None:
    # Налаштовуємо моки
    mock_internet.return_value = initial_value
    mock_valid_url.return_value = value_to_add

    # Викликаємо тестовану функцію
    url = "https://www.google.com"
    result = can_access_google_page(url)

    # Перевіряємо результат
    assert result == expected_value
