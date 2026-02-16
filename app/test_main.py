import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_valid, connection_valid, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(monkeypatch, url_valid, connection_valid, expected):
    monkeypatch.setattr("app.main.valid_google_url", lambda url
    : url_valid)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: connection_valid)
    assert can_access_google_page("https://google.com") == expected
    