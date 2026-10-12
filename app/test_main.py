import pytest

from app import main


@pytest.mark.parametrize(
    "has_connection, is_valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    has_connection: bool,
    is_valid_url: bool,
    expected: str,
) -> None:
    monkeypatch.setattr(
        main, "has_internet_connection", lambda: has_connection
    )
    monkeypatch.setattr(
        main, "valid_google_url", lambda url: is_valid_url
    )

    assert main.can_access_google_page("https://www.google.com") == expected
