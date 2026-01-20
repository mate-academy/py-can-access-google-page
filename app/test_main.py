import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page_scenarios(
        monkeypatch: pytest.MonkeyPatch,
        has_internet: bool,
        valid_url: bool,
        expected: str
) -> None:
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: has_internet
    )
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda url: valid_url
    )
    result = can_access_google_page("https://www.google.com")
    assert result == expected
