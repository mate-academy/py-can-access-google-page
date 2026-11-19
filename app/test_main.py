import pytest

from app import main


@pytest.mark.parametrize(
    "is_valid_url,has_connection,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "valid url and internet connection",
        "valid url without internet connection",
        "invalid url with internet connection",
        "invalid url without internet connection",
    ],
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    is_valid_url: bool,
    has_connection: bool,
    expected: str,
) -> None:
    def mock_valid_google_url(url: str) -> bool:
        return is_valid_url

    def mock_has_internet_connection() -> bool:
        return has_connection

    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(
        main,
        "has_internet_connection",
        mock_has_internet_connection,
    )

    assert main.can_access_google_page("https://www.google.com") == expected
