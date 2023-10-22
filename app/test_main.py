from app import main
import pytest
from typing import Callable
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_should_return_correct_result(
        monkeypatch: Callable,
        valid_google_url: bool,
        has_internet_connection: bool,
        expected: str
) -> None:
    def mocked_valid_google_url(url: str) -> bool:
        return valid_google_url

    def mocked_has_internet_connection() -> bool:
        return has_internet_connection

    monkeypatch.setattr(
        main,
        "has_internet_connection",
        mocked_has_internet_connection
    )
    monkeypatch.setattr(
        main,
        "valid_google_url",
        mocked_valid_google_url
    )

    assert can_access_google_page("url") == expected
