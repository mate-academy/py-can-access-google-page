import pytest
import requests
import app.main as main_module
from typing import Any, Protocol


# Визначаємо протокол для об'єкта, схожого на відповідь requests.Response
class ResponseLike(Protocol):
    status_code: int


def test_access_success(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Тест успішного доступу: підключення є, і requests.get повертає 200.
    Очікуваний результат: "Accessible".
    """
    monkeypatch.setattr(main_module, "has_internet_connection", lambda: True)

    def fake_get(url: str, timeout: int = 5) -> ResponseLike:
        class FakeResponse:
            status_code = 200
        return FakeResponse()

    # Мокуємо requests.get, щоб valid_google_url повертала True
    monkeypatch.setattr(requests, "get", fake_get)
    assert main_module.can_access_google_page(
        "https://www.google.com") == "Accessible"


def test_access_forbidden(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Тест забороненого доступу: підключення є, але requests.get повертає 403.
    Очікуваний результат: "Not accessible".
    """
    monkeypatch.setattr(main_module, "has_internet_connection", lambda: True)

    def fake_get(url: str, timeout: int = 5) -> ResponseLike:
        class FakeResponse:
            status_code = 403
        return FakeResponse()

    # Мокуємо requests.get, щоб valid_google_url повертала False
    monkeypatch.setattr(requests, "get", fake_get)
    assert main_module.can_access_google_page(
        "https://www.google.com") == "Not accessible"


def test_access_not_found(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Тест відсутності сторінки: підключення є, але requests.get повертає 404.
    Очікуваний результат: "Not accessible".
    """
    monkeypatch.setattr(main_module, "has_internet_connection", lambda: True)

    def fake_get(url: str, timeout: int = 5) -> ResponseLike:
        class FakeResponse:
            status_code = 404
        return FakeResponse()

    # Мокуємо requests.get, щоб valid_google_url повертала False
    monkeypatch.setattr(requests, "get", fake_get)
    assert main_module.can_access_google_page(
        "https://www.google.com") == "Not accessible"


def test_access_exception(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Тест винятку при доступі: підключення є, але requests.get викликає виняток.
    Очікуваний результат: RequestsException повинен бути піднятий,
    оскільки main.py не обробляє його.
    """
    monkeypatch.setattr(main_module, "has_internet_connection", lambda: True)

    # Мокуємо requests.get, щоб вона викидала виняток
    def fake_get_raises_exception(url: str, timeout: int = 5) -> Any:
        raise requests.exceptions.RequestException("Simulated error")

    monkeypatch.setattr(requests, "get", fake_get_raises_exception)

    # Очікуємо, що виняток буде викинутий з can_access_google_page
    with pytest.raises(requests.exceptions.RequestException):
        main_module.can_access_google_page("https://www.google.com")


def test_no_internet(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Тест відсутності інтернету: has_internet_connection повертає False.
    Очікуваний результат: "Not accessible" (незалежно від URL).
    """
    # Мокуємо has_internet_connection безпосередньо
    monkeypatch.setattr(main_module, "has_internet_connection", lambda: False)
    # valid_google_url не має викликатись завдяки short-circuiting 'and',
    # тому requests.get не потрібно мокувати в цьому тесті.
    assert main_module.can_access_google_page(
        "https://www.google.com") == "Not accessible"
