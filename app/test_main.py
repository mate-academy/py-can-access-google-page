from typing import Any

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "check_url, connection, access_to_google",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        monkeypatch: Any,
        check_url: bool,
        connection: bool,
        access_to_google: str
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda x: check_url)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: connection)

    assert can_access_google_page("google.com") == access_to_google
