import pytest
from _pytest.monkeypatch import MonkeyPatch
from typing import Callable
from unittest.mock import MagicMock
from app.main import can_access_google_page


@pytest.fixture
def url() -> str:
    return ("https://www.google.com/webhp?hl=en&sa="
            "X&ved=0ahUKEwjlr5aw25eFAxVFFBAIHbjlAdEQPAgJ")


@pytest.fixture
def mock_internet_connection(monkeypatch: MonkeyPatch) -> Callable:
    mock_internet_connection = MagicMock()
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_internet_connection
    )
    return mock_internet_connection


@pytest.fixture
def mock_valid_google_url(monkeypatch: MonkeyPatch) -> Callable:
    mock_valid_google_url = MagicMock()
    monkeypatch.setattr("app.main.valid_google_url", mock_valid_google_url)
    return mock_valid_google_url


@pytest.mark.parametrize(
    "connection_return,valid_url_return,expected_result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ],
    ids=[
        "can't access only with connection",
        "can't access only with valid url",
        "can't access with no connection and valid url",
        "can access with connection and valid url"
    ]
)
def test_can_access_google_page(
    url: str,
    mock_internet_connection: Callable,
    mock_valid_google_url: Callable,
    connection_return: bool,
    valid_url_return: bool,
    expected_result: str
) -> None:
    mock_internet_connection.return_value = connection_return
    mock_valid_google_url.return_value = valid_url_return
    assert can_access_google_page(url) == expected_result
