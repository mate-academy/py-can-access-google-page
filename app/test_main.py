import pytest
import app.main as module


def test_not_accessible_if_no_internet_connection(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(module, "valid_google_url", lambda url: True)
    monkeypatch.setattr(module, "has_internet_connection", lambda: False)

    result: str = module.can_access_google_page("https://google.com")

    assert result == "Not accessible"


def test_valid_url_and_connection_exists(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(module, "valid_google_url", lambda url: True)
    monkeypatch.setattr(module, "has_internet_connection", lambda: True)

    result: str = module.can_access_google_page("https://google.com")

    assert result == "Accessible"


def test_not_accessible_if_url_is_invalid(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(module, "valid_google_url", lambda url: False)
    monkeypatch.setattr(module, "has_internet_connection", lambda: True)

    result: str = module.can_access_google_page("https://google.com")

    assert result == "Not accessible"
