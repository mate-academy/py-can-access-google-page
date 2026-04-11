import pytest
from _pytest.monkeypatch import MonkeyPatch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    ("has_connection", "is_valid_url", "expected_result"),
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    monkeypatch: MonkeyPatch,
    has_connection: bool,
    is_valid_url: bool,
    expected_result: str,
) -> None:
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: has_connection,
    )
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda url: is_valid_url,
    )

    assert can_access_google_page("https://www.google.com") == expected_result
