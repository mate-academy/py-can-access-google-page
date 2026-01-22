import pytest
from _pytest.monkeypatch import MonkeyPatch

from app import main
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_google_url,has_internet_connection,result",
    [
        pytest.param(
            True, True, "Accessible",
            id="test_valid_url_and_connection_exists"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="test_valid_url_and_connection_not_exist"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="test_invalid_url_and_connection_exists"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="test_invalid_url_and_connection_not_exist"
        ),
    ]
)
def test_can_access_google_page(
        monkeypatch: MonkeyPatch,
        is_valid_google_url: bool,
        has_internet_connection: bool,
        result: str
) -> None:
    monkeypatch.setattr(
        main,
        "valid_google_url",
        lambda _: is_valid_google_url
    )
    monkeypatch.setattr(
        main,
        "has_internet_connection",
        lambda: has_internet_connection
    )
    assert can_access_google_page("abc") == result
