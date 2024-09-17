import pytest
from pytest import MonkeyPatch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    valid_url: bool,
    internet_connection: bool,
    expected: str,
    monkeypatch: MonkeyPatch
) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return valid_url
    monkeypatch.setattr(
        "app.main.valid_google_url", mock_valid_google_url
    )

    def mock_has_internet_connection() -> bool:
        return internet_connection
    monkeypatch.setattr(
        "app.main.has_internet_connection", mock_has_internet_connection
    )

    assert can_access_google_page(
        "https://home.google.com/welcome/"
    ) == expected
