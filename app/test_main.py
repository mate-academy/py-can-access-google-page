import pytest
from pytest import MonkeyPatch, fixture

from app.main import can_access_google_page


@pytest.fixture()
def valid_google_url_true(monkeypatch: MonkeyPatch) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return True
    monkeypatch.setattr("app.main.valid_google_url", mock_valid_google_url)


@pytest.fixture()
def valid_google_url_false(monkeypatch: MonkeyPatch) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return False
    monkeypatch.setattr("app.main.valid_google_url", mock_valid_google_url)


@pytest.fixture()
def has_internet_connection_true(monkeypatch: MonkeyPatch) -> None:
    def mock_has_internet_connection() -> bool:
        return True
    monkeypatch.setattr(
        "app.main.has_internet_connection", mock_has_internet_connection
    )


@pytest.fixture()
def has_internet_connection_false(monkeypatch: MonkeyPatch) -> None:
    def mock_has_internet_connection() -> bool:
        return False
    monkeypatch.setattr(
        "app.main.has_internet_connection", mock_has_internet_connection
    )


def test_should_return_accessible(
        valid_google_url_true: fixture,
        has_internet_connection_true: fixture
) -> None:
    assert can_access_google_page(
        "https://home.google.com/welcome/"
    ) == "Accessible"


def test_not_accessible_if_valid_url_is_false(
        valid_google_url_false: fixture,
        has_internet_connection_true: fixture
) -> None:
    assert can_access_google_page(
        "https://home.google.com/welcome/"
    ) == "Not accessible"


def test_not_accessible_if_internet_connection_is_false(
        valid_google_url_true: fixture,
        has_internet_connection_false: fixture
) -> None:
    assert can_access_google_page(
        "https://home.google.com/welcome/"
    ) == "Not accessible"
