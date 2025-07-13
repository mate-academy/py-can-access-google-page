import pytest
from _pytest.monkeypatch import MonkeyPatch

from app import main


@pytest.mark.parametrize(
    "valid_url,has_connection,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ],
    ids=[
        "Valid URL and has connection",
        "Valid URL and no connection",
        "Has connection but invalid URL"
    ]
)
def test_can_access_google_page(
        monkeypatch: MonkeyPatch,
        valid_url: bool,
        has_connection: bool,
        result: str
) -> None:

    def mock_valid_google_url(*args) -> bool:
        return valid_url

    def mock_has_internet_connection() -> bool:
        return has_connection

    monkeypatch.setattr(main, "valid_google_url", mock_valid_google_url)
    monkeypatch.setattr(
        main,
        "has_internet_connection",
        mock_has_internet_connection
    )
    assert main.can_access_google_page("https://google.com") == result
