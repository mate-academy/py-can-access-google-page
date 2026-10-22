import pytest
from _pytest.monkeypatch import MonkeyPatch

from app import main


@pytest.mark.parametrize(
    ("internet_connection", "valid_url", "expected_result"),
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_acess_google_page(
        monkeypatch: MonkeyPatch,
        internet_connection: bool,
        valid_url: bool,
        expected_result: str,
) -> None:
    url = "https://www.google.com"
    monkeypatch.setattr(
        main, "has_internet_connection", lambda: internet_connection
    )
    monkeypatch.setattr(
        main, "valid_google_url", lambda received: valid_url
    )

    assert main.can_access_google_page(url) == expected_result
