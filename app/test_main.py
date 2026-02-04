import pytest
import app.main as main


@pytest.mark.parametrize(
    "valid_url, has_internet, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        monkeypatch: pytest.MonkeyPatch,
        valid_url: bool,
        has_internet: bool,
        result: str
) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: valid_url)
    monkeypatch.setattr(main, "has_internet_connection", lambda: has_internet)
    assert main.can_access_google_page("any") == result
