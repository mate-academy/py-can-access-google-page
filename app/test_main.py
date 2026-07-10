import app.main


from typing import Any


from app.main import can_access_google_page


def mock_true(*args, **kwargs) -> bool:
    return True


def mock_false(*args, **kwargs) -> bool:
    return False


def test_returns_accessible_if_url_valid_and_has_internet(
    monkeypatch: Any
) -> None:
    monkeypatch.setattr(app.main, "valid_google_url", mock_true)
    monkeypatch.setattr(app.main, "has_internet_connection", mock_true)

    assert can_access_google_page("https://google.com") == "Accessible"


def test_returns_not_accessible_if_url_not_valid(
    monkeypatch: Any
) -> None:
    monkeypatch.setattr(app.main, "valid_google_url", mock_false)
    monkeypatch.setattr(app.main, "has_internet_connection", mock_true)

    assert can_access_google_page("https://google.com") == "Not accessible"


def test_returns_not_accessible_if_no_connection(
    monkeypatch: Any
) -> None:
    monkeypatch.setattr(app.main, "valid_google_url", mock_true)
    monkeypatch.setattr(app.main, "has_internet_connection", mock_false)

    assert can_access_google_page("https://google.com") == "Not accessible"
