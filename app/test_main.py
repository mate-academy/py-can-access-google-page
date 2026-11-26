import pytest
from _pytest.monkeypatch import MonkeyPatch

from app import main


@pytest.mark.parametrize(
    "is_valid_url, has_connection, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
        monkeypatch: MonkeyPatch,
        is_valid_url: bool,
        has_connection: bool,
        expected: str
) -> None:
    monkeypatch.setattr(
        main,
        "valid_google_url",
        lambda url: is_valid_url
    )
    monkeypatch.setattr(
        main,
        "has_internet_connection",
        lambda: has_connection
    )

    result = main.can_access_google_page(
        "https://www.google.com"
    )

    assert result == expected
