from pytest import mark, MonkeyPatch

from app.main import can_access_google_page


URL = "http//google.com.ua"


@mark.parametrize(
    "val_url, val_connection, result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible"),
    ],
    ids=[
        "True + False : access will be denied",
        "False + True : access will be denied",
        "False + False : access will be denied",
        "True + True : access will be granted",
    ],
)
def test_can_access_google_page(
        monkeypatch: MonkeyPatch,
        val_url: bool,
        val_connection: bool,
        result: str
) -> None:

    monkeypatch.setattr(
        "app.main.has_internet_connection", lambda *args: val_connection
    )
    monkeypatch.setattr(
        "app.main.valid_google_url", lambda *args: val_url
    )

    assert can_access_google_page(URL) == result
