import pytest
from app import main


@pytest.mark.parametrize(
    "url,is_valid_url,has_connection,expected",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://google.com", True, False, "Not accessible"),
        ("https://google.com", False, True, "Not accessible"),
        ("https://google.com", False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    monkeypatch: pytest.MonkeyPatch,
    url: str,
    is_valid_url: bool,
    has_connection: bool,
    expected: str,
) -> None:

    monkeypatch.setattr(
        main,
        "valid_google_url",
        lambda x: is_valid_url,
    )

    monkeypatch.setattr(
        main,
        "has_internet_connection",
        lambda: has_connection,
    )

    assert main.can_access_google_page(url) == expected
