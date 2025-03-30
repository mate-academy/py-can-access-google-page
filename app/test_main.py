import pytest
from unittest.mock import Mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, has_connection, expected",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://google.com", False, True, "Not accessible"),
        ("https://google.com", True, False, "Not accessible"),
        ("https://notgoogle.com", False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    url: str,
    valid_url: bool,
    has_connection: bool,
    expected: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url", Mock(return_value=valid_url)
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection", Mock(return_value=has_connection)
    )

    assert can_access_google_page(url) == expected
