import pytest

import app
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_valid, internet_connection, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")

    ]
)
def test_can_access_google_page(
        monkeypatch: pytest.MonkeyPatch,
        url_valid: bool,
        internet_connection: bool,
        expected: str
) -> None:
    monkeypatch.setattr(
        app.main,
        "valid_google_url",
        lambda url: url_valid
    )
    monkeypatch.setattr(
        app.main,
        "has_internet_connection",
        lambda: internet_connection
    )
    assert can_access_google_page(url="https://google.com") == expected
