
import pytest

from app import main


@pytest.mark.parametrize(
    "internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    internet: bool,
    valid_url: bool,
    expected: str,
) -> None:
    monkeypatch.setattr(
        main, "has_internet_connection", lambda: internet
    )
    monkeypatch.setattr(
        main, "valid_google_url", lambda url: valid_url
    )

    result = main.can_access_google_page("https://www.google.com")

    assert result == expected
