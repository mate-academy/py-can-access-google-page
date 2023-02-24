from pytest import mark, MonkeyPatch

from app.main import can_access_google_page

URL = "Google url"


@mark.parametrize(
    "valid_url, connected, can_access",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "True + True -> must be Accessible",
        "True + False -> must be Not accessible",
        "False + True -> must be Not accessible",
        "False + False -> must be Not accessible",
    ],
)
def test_can_access_google_page(
    monkeypatch: MonkeyPatch, valid_url: bool, connected: bool, can_access: str
) -> None:
    monkeypatch.setattr(
        "app.main.has_internet_connection", lambda *args: connected
    )
    monkeypatch.setattr(
        "app.main.valid_google_url", lambda *args: valid_url
    )
    assert can_access_google_page(URL) == can_access
