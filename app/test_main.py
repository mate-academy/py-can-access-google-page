import pytest
import app.main as main_module
import requests
from typing import Protocol


class ResponseLike(Protocol):
    status_code: int


def test_access_success(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main_module, "has_internet_connection", lambda: True)

    def fake_get(url: str, timeout: int = 5) -> ResponseLike:
        class FakeResponse:
            status_code = 200
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)
    assert main_module.can_access_google_page(
        "https://www.google.com") == "Accessible"


def test_access_forbidden(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main_module, "has_internet_connection", lambda: True)

    def fake_get(url: str, timeout: int = 5) -> ResponseLike:
        class FakeResponse:
            status_code = 403
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)
    assert main_module.can_access_google_page(
        "https://www.google.com") == "Not accessible"


def test_access_not_found(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main_module, "has_internet_connection", lambda: True)

    def fake_get(url: str, timeout: int = 5) -> ResponseLike:
        class FakeResponse:
            status_code = 404
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)
    assert main_module.can_access_google_page(
        "https://www.google.com") == "Not accessible"


def test_access_exception(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main_module, "has_internet_connection", lambda: True)

    def fake_valid_google_url(url: str) -> None:
        raise requests.exceptions.RequestException("Simulated error")

    monkeypatch.setattr(main_module, "valid_google_url", fake_valid_google_url)

    with pytest.raises(requests.exceptions.RequestException):
        main_module.can_access_google_page("https://www.google.com")


def test_no_internet(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main_module, "has_internet_connection", lambda: False)
    assert main_module.can_access_google_page(
        "https://www.google.com") == "Not accessible"
