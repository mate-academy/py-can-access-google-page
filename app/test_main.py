from _pytest.monkeypatch import MonkeyPatch

from app.main import can_access_google_page


def test_can_access_google_page(monkeypatch: MonkeyPatch) -> None:
    # Mock the valid_google_url function to always return True
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)

    # Mock the has_internet_connection function to always return True
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    # Test with a valid Google URL
    assert can_access_google_page("https://www.google.com") == "Accessible"


def test_cannot_access_google_page(monkeypatch: MonkeyPatch) -> None:
    # Test with an invalid URL
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)
    monkeypatch.setattr("app.main.valid_google_url", lambda url: False)
    assert (
        can_access_google_page("https://www.invalidurl.com")
        == "Not accessible"
    )

    # Test with a valid URL but no internet connection
    monkeypatch.setattr("app.main.valid_google_url", lambda url: True)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: False)
    assert can_access_google_page("https://www.google.com") == "Not accessible"
