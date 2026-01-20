import pytest
from _pytest.monkeypatch import MonkeyPatch

from app import main
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_result,connection_result,result_can_access_google_page",
    [
        pytest.param(True, True, "Accessible",
                     id="valid url and time, is accessible"),
        pytest.param(True, False, "Not accessible",
                     id="valid url and not valid time, not accessible"),
        pytest.param(False, True, "Not accessible",
                     id="not valid url and valid time, not accessible"),
        pytest.param(False, False, "Not accessible",
                     id="not valid url and time, not accessible")
    ]
)
def test_can_access_google_page(
        monkeypatch: MonkeyPatch,
        url_result: bool,
        connection_result: bool,
        result_can_access_google_page: str
) -> None:
    monkeypatch.setattr(
        main,
        "valid_google_url",
        lambda _: url_result
    )
    monkeypatch.setattr(
        main,
        "has_internet_connection",
        lambda: connection_result
    )
    assert can_access_google_page("google") == result_can_access_google_page
