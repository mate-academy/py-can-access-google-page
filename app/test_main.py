import pytest
from pytest import MonkeyPatch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_internet, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_valid_url_and_connection_exists(
        monkeypatch: MonkeyPatch,
        valid_url: bool,
        has_internet: bool,
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
    assert can_access_google_page("any_url") == expected
