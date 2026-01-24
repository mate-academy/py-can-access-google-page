import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, has_internet, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    monkeypatch,
    is_valid_url: bool,
    has_internet: bool,
    expected: str,
) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda _: is_valid_url,
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: has_internet,
    )

    result = can_access_google_page("https://www.google.com")

    assert result == expected
