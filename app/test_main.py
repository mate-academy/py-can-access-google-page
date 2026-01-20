import pytest
import datetime
import requests

from app.main import can_access_google_page


@pytest.fixture
def mock_has_internet_true(monkeypatch: pytest.MonkeyPatch) -> None:
    class DatetimeMock(datetime.datetime):
        @classmethod
        def now(cls) -> datetime.datetime:
            fake_time = datetime.datetime(2023, 10, 19, 12, 12, 12)
            return fake_time

    monkeypatch.setattr(datetime, "datetime", DatetimeMock)


@pytest.fixture
def mock_valid_url_true(monkeypatch: pytest.MonkeyPatch) -> None:

    def mock_get(url: str) -> requests.Response:
        response = requests.Response()
        response.status_code = 200
        return response

    monkeypatch.setattr(requests, "get", mock_get)


@pytest.fixture
def mock_has_internet_false(monkeypatch: pytest.MonkeyPatch) -> None:
    class DatetimeMock(datetime.datetime):
        @classmethod
        def now(cls) -> datetime.datetime:
            fake_time = datetime.datetime(2023, 10, 19, 23, 59, 59)
            return fake_time

    monkeypatch.setattr(datetime, "datetime", DatetimeMock)


@pytest.fixture
def mock_valid_url_false(monkeypatch: pytest.MonkeyPatch) -> None:

    def mock_get(url: str) -> requests.Response:
        response = requests.Response()
        response.status_code = 404
        return response

    monkeypatch.setattr(requests, "get", mock_get)


def test_can_access_google_page_both_functions_return_true(
        mock_valid_url_true: callable,
        mock_has_internet_true: callable) -> None:
    google_url = "https://www.google.com/"
    assert can_access_google_page(google_url) == "Accessible"


def test_can_access_google_page_both_functions_return_false(
        mock_valid_url_false: callable,
        mock_has_internet_false: callable) -> None:
    google_url = "https://www.google.com/"
    assert can_access_google_page(google_url) == "Not accessible"


def test_can_access_google_page_only_valid_url_returns_true(
        mock_valid_url_true: callable,
        mock_has_internet_false: callable) -> None:
    google_url = "https://www.google.com/"
    assert can_access_google_page(google_url) == "Not accessible"


def test_can_access_google_page_only_has_connection_returns_true(
        mock_valid_url_false: callable,
        mock_has_internet_true: callable) -> None:
    google_url = "https://www.google.com/"
    assert can_access_google_page(google_url) == "Not accessible"
