from typing import Callable
from app.main import can_access_google_page


def test_true_url_true_time(monkeypatch: Callable) -> None:
    monkeypatch.setattr("app.main.valid_google_url",
                        lambda *args: True)
    monkeypatch.setattr("app.main.has_internet_connection",
                        lambda *args: True)
    assert can_access_google_page("x") == "Accessible"


def test_false_url_false_time(monkeypatch: Callable) -> None:
    monkeypatch.setattr("app.main.valid_google_url",
                        lambda *args: False)
    monkeypatch.setattr("app.main.has_internet_connection",
                        lambda *args: False)
    assert can_access_google_page("x") == "Not accessible"


def test_true_url_false_time(monkeypatch: Callable) -> None:
    monkeypatch.setattr("app.main.valid_google_url",
                        lambda *args: True)
    monkeypatch.setattr("app.main.has_internet_connection",
                        lambda *args: False)
    assert can_access_google_page("x") == "Not accessible"


def test_false_url_true_time(monkeypatch: Callable) -> None:
    monkeypatch.setattr("app.main.valid_google_url",
                        lambda *args: False)
    monkeypatch.setattr("app.main.has_internet_connection",
                        lambda *args: True)
    assert can_access_google_page("x") == "Not accessible"
