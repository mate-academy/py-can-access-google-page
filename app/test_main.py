import pytest
from app.main import can_access_google_page
from _pytest.monkeypatch import MonkeyPatch


@pytest.mark.parametrize(
    "url,"
    " valid_url,"
    " internet_connection,"
    " expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.invalidurl.com", False, True, "Not accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.invalidurl.com", False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        monkeypatch: MonkeyPatch,
        url: str,
        valid_url: bool,
        internet_connection: bool,
        expected_result: str) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return valid_url

    def mock_has_internet_connection() -> bool:
        return internet_connection

    monkeypatch.setattr("app.main.valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(
        "app.main.has_internet_connection", mock_has_internet_connection
    )

    result = can_access_google_page(url)

    assert result == expected_result
