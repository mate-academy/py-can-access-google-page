import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection, valid_url, expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="test if OK"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="test invalid url"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="test no connection"
        ),
        pytest.param(
            False,
            False,
            "Not accessible", id="test no connection & invalid url"
        )
    ]
)
def test_can_access(
        monkeypatch: pytest.MonkeyPatch,
        connection: bool,
        valid_url: bool,
        expected: str
) -> None:
    monkeypatch.setattr("app.main.has_internet_connection", lambda: connection)
    monkeypatch.setattr("app.main.valid_google_url", lambda _: valid_url)

    result = can_access_google_page("http://google.com")
    assert result == expected
