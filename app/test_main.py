import pytest
from _pytest.monkeypatch import MonkeyPatch

import app.main


@pytest.mark.parametrize(
    "valid_url, has_connection, expected",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
    ],
    ids=[
        "Should return 'Accessible' if connection and valid url both True",
        "Should return 'Not accessible' if connection and valid url is False",
        "Should return 'Not accessible' if valid url is False",
        "Should return 'Not accessible' if connection is False",
    ]
)
def test_can_access_google_page(
        monkeypatch: MonkeyPatch,
        valid_url: bool,
        has_connection: bool,
        expected: str
) -> None:
    monkeypatch.setattr(app.main,
                        "valid_google_url",
                        lambda url: valid_url)
    monkeypatch.setattr(app.main,
                        "has_internet_connection",
                        lambda: has_connection)

    assert (
        app.main.can_access_google_page(
            "https://www.google.com.ua/"
        ) == expected
    )
