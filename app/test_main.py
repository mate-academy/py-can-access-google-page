from app.main import can_access_google_page

import pytest


@pytest.mark.parametrize(
    "valid_google_url,has_internet_connection,expected_result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
    ]
)
def test_can_access_google_page(monkeypatch: pytest.MonkeyPatch,
                                valid_google_url: bool,
                                has_internet_connection: bool,
                                expected_result: str
                                ) -> None:
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda *args: valid_google_url
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda *args: has_internet_connection
    )
    assert can_access_google_page("https://google.com") == expected_result
