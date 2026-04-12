import pytest
from app.main import can_access_google_page
@pytest.mark.parametrize(
    "valid,internet,expected",
    [
        (True,  True,  "Accessible"),
        (True,  False, "Not accessible"),
        (False, True,  "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_all_cases(monkeypatch, valid, internet, expected):
    monkeypatch.setattr("app.main.valid_google_url", lambda url: valid)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: internet)
    assert can_access_google_page("any url") == expected


