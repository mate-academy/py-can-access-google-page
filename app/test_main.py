import pytest


from app import main


@pytest.mark.parametrize(
    ("connection", "valid", "expected"),
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    connection: bool,
    valid: bool,
    expected: str,
) -> None:
    monkeypatch.setattr(main, "has_internet_connection", lambda: connection)
    monkeypatch.setattr(main, "valid_google_url", lambda _url: valid)

    assert main.can_access_google_page("https://google.com") == expected
