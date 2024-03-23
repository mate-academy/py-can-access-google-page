import pytest

from _pytest.monkeypatch import MonkeyPatch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, expected_status",
    [
        ("https://www.google.com", "Not accessible"),
        ("https://www.google.com", "Not accessible"),
        ("https://www.google.com", "Not accessible")
    ]
)
def test_cannot_access_if_connection_or_valid_url_is_true(
        monkeypatch: MonkeyPatch,
        url: str,
        expected_status: str
) -> None:
    monkeypatch.setattr(
        "app.main.has_internet_connection", lambda: False
    )
    monkeypatch.setattr(
        "app.main.valid_google_url", lambda url: False
    )
    assert can_access_google_page(url) == expected_status


@pytest.mark.parametrize(
    "url, expected_status",
    [
        ("https://www.google.com", "Not accessible"),
        ("https://www.google.com", "Not accessible")
    ]
)
def test_cannot_access_if_only_connection(
        monkeypatch: MonkeyPatch,
        url: str,
        expected_status: str
) -> None:
    monkeypatch.setattr(
        "app.main.has_internet_connection", lambda: False
    )
    assert can_access_google_page(url) == expected_status


@pytest.mark.parametrize(
    "url, expected_status",
    [
        ("https://www.google.com", "Not accessible"),
        ("https://www.google.com", "Not accessible")
    ]
)
def test_cannot_access_if_only_valid_url(
        monkeypatch: MonkeyPatch,
        url: str,
        expected_status: str
) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url", lambda url: False
    )
    assert can_access_google_page(url) == expected_status
