from typing import Dict
from unittest.mock import Mock

import pytest
from _pytest.monkeypatch import MonkeyPatch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, has_net, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page_result(
    monkeypatch: MonkeyPatch,
    is_valid_url: bool,
    has_net: bool,
    expected: str,
) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url", lambda url: is_valid_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection", lambda: has_net
    )

    result = can_access_google_page("https://www.google.com")
    assert result == expected


def test_can_access_google_page_passes_url_to_validator(
    monkeypatch: MonkeyPatch,
) -> None:
    passed: Dict[str, str] = {}

    def fake_valid(url: str) -> bool:
        passed["url"] = url
        return True

    monkeypatch.setattr("app.main.valid_google_url", fake_valid)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    test_url = "https://www.google.com/"
    result = can_access_google_page(test_url)

    assert result == "Accessible"
    assert passed["url"] == test_url


def test_short_circuit_when_no_internet(
    monkeypatch: MonkeyPatch,
) -> None:
    mock_has_net = Mock(return_value=False)
    mock_valid_url = Mock(return_value=True)

    monkeypatch.setattr("app.main.has_internet_connection", mock_has_net)
    monkeypatch.setattr("app.main.valid_google_url", mock_valid_url)

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"
    mock_has_net.assert_called_once_with()
    mock_valid_url.assert_not_called()


def test_calls_dependencies_and_returns_accessible(
    monkeypatch: MonkeyPatch,
) -> None:
    url = "https://www.google.com"
    mock_has_net = Mock(return_value=True)
    mock_valid_url = Mock(return_value=True)

    monkeypatch.setattr("app.main.has_internet_connection", mock_has_net)
    monkeypatch.setattr("app.main.valid_google_url", mock_valid_url)

    result = can_access_google_page(url)

    assert result == "Accessible"
    mock_has_net.assert_called_once_with()
    mock_valid_url.assert_called_once_with(url)
