import pytest
from app import main


@pytest.mark.parametrize(
    "url_valid, internet_available, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    url_valid: bool,
    internet_available: bool,
    expected: str,
) -> None:
    monkeypatch.setattr(
        main,
        "valid_google_url",
        lambda url: url_valid,
    )

    monkeypatch.setattr(
        main,
        "has_internet_connection",
        lambda: internet_available,
    )

    result = main.can_access_google_page(
        "https://www.google.com"
    )

    assert result == expected
