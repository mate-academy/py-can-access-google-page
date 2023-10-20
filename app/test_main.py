import pytest
import datetime
import requests

from app.main import can_access_google_page


monkeypatch = pytest.MonkeyPatch()
fake_time = datetime.datetime(2023, 10, 19, 12, 12, 12)


def test_can_access_google_page(monkeypatch: object) -> None:
    class DatetimeMock(datetime.datetime):
        @classmethod
        def now(cls) -> datetime.datetime:
            return fake_time

    def mock_get(url: str) -> requests.Response:
        response = requests.Response()
        response.status_code = 200
        return response

    monkeypatch.setattr(datetime, "datetime", DatetimeMock)
    monkeypatch.setattr(requests, "get", mock_get)
    google_url = "https://www.google.com/"
    assert can_access_google_page(google_url) == "Accessible"
