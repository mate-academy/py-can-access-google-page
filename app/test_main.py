import pytest

from app import main


@pytest.mark.parametrize(
    "is_valid_url, has_internet, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    is_valid_url: bool,
    has_internet: bool,
    expected: str,
) -> None:
    def mock_valid_google_url(_url: str) -> bool:
        return is_valid_url

    def mock_has_internet_connection() -> bool:
        return has_internet

    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(main, "has_internet_connection",
                        mock_has_internet_connection)

    assert main.can_access_google_page("https://google.com") == expected
