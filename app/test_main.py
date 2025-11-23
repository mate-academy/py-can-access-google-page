import pytest
from _pytest.monkeypatch import MonkeyPatch

from app import main


@pytest.mark.parametrize(
    "valid_value, internet_value, expected_result",
    (
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    )
)
def test_can_access_google_page_handles_all_scenarios(
        valid_value: bool,
        internet_value: bool,
        expected_result: str,
        monkeypatch: MonkeyPatch) -> None:
    def fake_valid(url: str) -> bool:
        return valid_value

    def fake_internet() -> bool:
        return internet_value

    monkeypatch.setattr("app.main.valid_google_url", fake_valid)
    monkeypatch.setattr("app.main.has_internet_connection", fake_internet)
    assert (main.can_access_google_page
            ("https://www.google.com") == expected_result)
