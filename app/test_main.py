import pytest

from app.main import can_access_google_page
from _pytest.monkeypatch import MonkeyPatch


@pytest.mark.parametrize(
    "valid_url_return,has_internet_return,expected_result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ]
)
def test_can_access_google_page_if_both_true(
        monkeypatch: MonkeyPatch,
        valid_url_return: bool,
        has_internet_return: bool,
        expected_result: str
) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return valid_url_return

    def mock_has_internet_connection() -> bool:
        return has_internet_return
    monkeypatch.setattr(
        "app.main.valid_google_url",
        mock_valid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        mock_has_internet_connection
    )
    assert can_access_google_page(
        "https://www.google.com/"
    ) == expected_result
