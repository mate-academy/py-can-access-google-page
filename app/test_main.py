import pytest
import app.main as main


@pytest.mark.parametrize(
    "result_valid_url, result_has_internet, result_can_access",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible")
    ]
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    result_valid_url: bool,
    result_has_internet: bool,
    result_can_access: str
) -> None:
    url = "google"

    def monkey_valid_google_url(url: str) -> bool:
        return result_valid_url

    def monkey_has_internet_connection() -> bool:
        return result_has_internet

    monkeypatch.setattr(main, "valid_google_url", monkey_valid_google_url)
    monkeypatch.setattr(
        main, "has_internet_connection", monkey_has_internet_connection
    )
    assert main.can_access_google_page(url) == result_can_access
