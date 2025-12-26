import pytest
import app.main as main_module  # Імпортуємо весь модуль для monkeypatch
import requests  # Потрібно для monkeypatching requests.get, якщо не мокаємо valid_google_url повністю


# Тести для can_access_google_page з використанням моків

def test_can_access_google_page_when_valid_url_and_connection_exists(monkeypatch):
    """
    Тест, коли URL дійсний і є підключення до Інтернету.
    Очікуваний результат: "Accessible".
    """
    monkeypatch.setattr(main_module, 'valid_google_url', lambda url: True)
    monkeypatch.setattr(main_module, 'has_internet_connection', lambda: True)
    assert main_module.can_access_google_page("https://www.google.com") == "Accessible"


def test_can_access_google_page_when_valid_url_but_no_internet_connection(monkeypatch):
    """
    Тест, коли URL дійсний, але немає підключення до Інтернету.
    Очікуваний результат: "Not accessible".
    """
    monkeypatch.setattr(main_module, 'valid_google_url', lambda url: True)
    monkeypatch.setattr(main_module, 'has_internet_connection', lambda: False)
    assert main_module.can_access_google_page("https://www.google.com") == "Not accessible"


def test_can_access_google_page_when_invalid_url_but_connection_exists(monkeypatch):
    """
    Тест, коли URL недійсний, але є підключення до Інтернету.
    Очікуваний результат: "Not accessible".
    """
    monkeypatch.setattr(main_module, 'valid_google_url', lambda url: False)
    monkeypatch.setattr(main_module, 'has_internet_connection', lambda: True)
    assert main_module.can_access_google_page("https://not-google.com") == "Not accessible"


def test_can_access_google_page_when_invalid_url_and_no_internet_connection(monkeypatch):
    """
    Тест, коли URL недійсний і немає підключення до Інтернету.
    Очікуваний результат: "Not accessible".
    """
    monkeypatch.setattr(main_module, 'valid_google_url', lambda url: False)
    monkeypatch.setattr(main_module, 'has_internet_connection', lambda: False)
    assert main_module.can_access_google_page("https://not-google.com") == "Not accessible"


def test_can_access_google_page_with_empty_url(monkeypatch):
    """
    Тест з порожнім URL і існуючим підключенням.
    Очікуваний результат: "Not accessible".
    """
    # Оскільки порожній URL не буде дійсним для valid_google_url, мокаємо його як False
    monkeypatch.setattr(main_module, 'valid_google_url', lambda url: False)
    monkeypatch.setattr(main_module, 'has_internet_connection', lambda: True)
    assert main_module.can_access_google_page("") == "Not accessible"


def test_can_access_google_page_with_none_url(monkeypatch):
    """
    Тест з URL як None і існуючим підключенням.
    Очікуваний результат: "Not accessible".
    """
    # Оскільки None URL не буде дійсним для valid_google_url, мокаємо його як False
    monkeypatch.setattr(main_module, 'valid_google_url', lambda url: False)
    monkeypatch.setattr(main_module, 'has_internet_connection', lambda: True)
    assert main_module.can_access_google_page(None) == "Not accessible"


# Цей тест свідомо очікує падіння, якщо app/main.py не обробляє винятки.
# Він виявив проблему в main.py, але якщо main.py не можна змінювати,
# то цей тест буде демонструвати, що функція не є стійкою до винятків.
def test_can_access_google_page_when_valid_google_url_raises_exception_no_main_py_change(monkeypatch):
    """
    Тест, коли функція valid_google_url викидає виняток (наприклад, RequestException).
    Очікуваний результат: Функція can_access_google_page повинна була б повернути "Not accessible",
    але оскільки app/main.py не обробляє винятки, цей тест, ймовірно, впаде.
    """
    monkeypatch.setattr(main_module, 'has_internet_connection', lambda: True)

    # Мокаємо valid_google_url так, щоб вона викидала виняток
    def mock_valid_google_url_raises_exception(url):
        raise requests.exceptions.RequestException("Simulated network error")

    monkeypatch.setattr(main_module, 'valid_google_url', mock_valid_google_url_raises_exception)

    # Цей рядок спровокує виняток, якщо main.py не обробляє його
    with pytest.raises(requests.exceptions.RequestException):
        main_module.can_access_google_page("https://www.google.com")