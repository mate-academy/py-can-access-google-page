import pytest

from app import main


@pytest.mark.parametrize(
    ("connection_available", "url_is_valid", "expected_result"),
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    connection_available: bool,
    url_is_valid: bool,
    expected_result: str,
) -> None:
    monkeypatch.setattr(
        main, "has_internet_connection", lambda: connection_available
    )
    monkeypatch.setattr(main, "valid_google_url", lambda url: url_is_valid)

    assert main.can_access_google_page("https://google.com") == expected_result
