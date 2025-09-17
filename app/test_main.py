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
    monkeypatch.setattr("app.main.valid_google_url", lambda url: is_valid_url)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: has_net)

    assert can_access_google_page("https://www.google.com") == expected


def test_can_access_google_page_passes_url_to_validator(
    monkeypatch: MonkeyPatch,
) -> None:
    passed = {}

    def fake_valid(url: str) -> bool:
        passed["url"] = url
        return True

    monkeypatch.setattr("app.main.valid_google_url", fake_valid)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: True)

    test_url = "https://www.google.com/"
    assert can_access_google_page(test_url) == "Accessible"
    assert passed["url"] == test_url
