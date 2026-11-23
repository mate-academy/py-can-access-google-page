import pytest

import app.main as main


@pytest.mark.parametrize(
    "url_is_valid, internet, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    url_is_valid: bool,
    internet: bool,
    expected: str
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: url_is_valid)
    monkeypatch.setattr(main, "has_internet_connection", lambda: internet)
    assert main.can_access_google_page("https://www.google.com") == expected
