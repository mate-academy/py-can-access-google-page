from unittest import mock
from typing import Callable
import pytest


from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_calls_both_functions(
    mocked_has_internet_connection: mock.MagicMock,
    mocked_valid_google_url: mock.MagicMock
) -> None:
    can_access_google_page("url::some_url")
    mocked_valid_google_url.assert_called_once_with(
        "url::some_url"
    )
    mocked_has_internet_connection.assert_called_once()


@pytest.fixture()
def mock_returns_true() -> Callable:
    def returns_true(url: str = "optional") -> bool:
        return True

    return returns_true


@pytest.fixture()
def mock_returns_false() -> Callable:
    def returns_false(url: str = "optional") -> bool:
        return False

    return returns_false


def test_returns_not_accessible_on_both_false(
    monkeypatch: pytest.MonkeyPatch,
    mock_returns_false: Callable
) -> None:

    monkeypatch.setattr(
        "app.main.valid_google_url",
        mock_returns_false
    )

    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_returns_false
    )

    assert can_access_google_page("") == "Not accessible"


def test_invalid_url_and_no_connection_returns_not_accessible(
    monkeypatch: pytest.MonkeyPatch,
    mock_returns_false: Callable,
    mock_returns_true: Callable
) -> None:

    monkeypatch.setattr(
        "app.main.valid_google_url",
        mock_returns_true
    )

    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_returns_false
    )

    assert can_access_google_page("") == "Not accessible"


def test_returns_not_accessible_on_invalid_url(
    monkeypatch: pytest.MonkeyPatch,
    mock_returns_false: Callable,
    mock_returns_true: Callable
) -> None:

    monkeypatch.setattr(
        "app.main.valid_google_url",
        mock_returns_false
    )

    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_returns_true
    )

    assert can_access_google_page("") == "Not accessible"


def test_valid_url_and_connection_exists_returns_accessible(
    monkeypatch: pytest.MonkeyPatch,
    mock_returns_true: Callable
) -> None:

    monkeypatch.setattr(
        "app.main.valid_google_url",
        mock_returns_true
    )

    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_returns_true
    )

    assert can_access_google_page("") == "Accessible"
