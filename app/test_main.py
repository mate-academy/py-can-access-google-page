import pytest
from app import main


@pytest.mark.parametrize(
    "mock_internet, mock_url, expected_result",
    [
        (True, True, "Accessible"),          # Оба условия верны
        (True, False, "Not accessible"),     # Только интернет есть
        (False, True, "Not accessible"),     # Только URL валидный
        (False, False, "Not accessible"),    # Ничего не верно
    ],
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    mock_internet: bool,
    mock_url: bool,
    expected_result: str,
) -> None:
    # Подменяем внутренние функции через monkeypatch
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: mock_internet,
    )
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda url: mock_url,
    )

    # Вызываем целевую функцию через импортированный модуль main
    result = main.can_access_google_page("https://google.com")
    assert result == expected_result
