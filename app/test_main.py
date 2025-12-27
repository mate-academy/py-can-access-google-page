import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, connection, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "valid url and connected",
        "invalid url and connected",
        "valid url and not connected",
        "invalid url and not connected"
    ]
)
def test_can_access_google_page(
        monkeypatch: pytest.MonkeyPatch,
        valid_url: bool,
        connection: bool,
        result: str
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda url: valid_url)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: connection)
    assert can_access_google_page("some_valid_url") == result
