import pytest

from app.main import can_access_google_page

TEST_URL = "fake_url"


@pytest.mark.parametrize(
    "has_internet, valid_url, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page_with_monkeypatch(
    monkeypatch: pytest.MonkeyPatch,
    has_internet: bool,
    valid_url: bool,
    expected_result: str
) -> None:
    def fake_valid_google_url(url: str) -> bool:
        return valid_url

    def fake_has_internet_connection() -> bool:
        return has_internet

    monkeypatch.setattr(
        "app.main.valid_google_url",
        fake_valid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        fake_has_internet_connection
    )

    assert can_access_google_page(url=TEST_URL) == expected_result
