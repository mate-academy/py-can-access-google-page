import pytest

from app import main
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection,is_valid_url,url,expected_result",
    [
        (True, True, "https://www.google.com", "Accessible"),
        (False, True, "https://www.google.com", "Not accessible"),
        (True, False, "https://www.google", "Not accessible"),
        (False, False, "https://www.google", "Not accessible")
    ],
    ids=[
        "if has internet connection and valid url return Accessible",
        "if no internet connection and valid url return Not accessible",
        "if has internet connection and not valid url return Not accessible",
        "if no internet connection and not valid url return Not accessible"
    ]
)
def test_can_access_google_page(
        monkeypatch: pytest.MonkeyPatch,
        has_internet_connection: bool,
        is_valid_url: bool,
        url: str,
        expected_result: str
) -> None:
    monkeypatch.setattr(
        main,
        "has_internet_connection",
        lambda: has_internet_connection
    )
    monkeypatch.setattr(main, "valid_google_url", lambda _: is_valid_url)
    assert can_access_google_page(url) == expected_result
