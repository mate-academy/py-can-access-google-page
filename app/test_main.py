import pytest
from app import main


@pytest.mark.parametrize(
    "is_valid_url, has_internet_connection, expected",
    [
        pytest.param(True, True, "Accessible"),
        pytest.param(True, False, "Not accessible"),
        pytest.param(False, True, "Not accessible"),
        pytest.param(False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(monkeypatch: pytest.MonkeyPatch,
                                is_valid_url: bool,
                                has_internet_connection: bool,
                                expected: str) -> None:
    monkeypatch.setattr(main, "valid_google_url", lambda url: is_valid_url)
    monkeypatch.setattr(main, "has_internet_connection",
                        lambda: has_internet_connection)

    assert (main.can_access_google_page("https://www.google.com")
            == expected)
