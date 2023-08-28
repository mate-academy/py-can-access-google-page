import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "functions_result, response",
    [
        pytest.param(
            [True, True],
            "Accessible",
            id="Should return 'Accessible' if both funcs return True",
        ),
        pytest.param(
            [False, True],
            "Not accessible",
            id="Should return 'Not accessible' if invalid url",
        ),
        pytest.param(
            [True, False],
            "Not accessible",
            id="Should return 'Not accessible' if no connection",
        ),
        pytest.param(
            [False, False],
            "Not accessible",
            id="Should return 'Not accessible' if both funcs return False",
        ),
    ],
)
def test_can_access_google_page_with_different_url_and_connection_status(
    functions_result: list[bool], response: str
) -> None:
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(
        "app.main.valid_google_url", lambda *args: functions_result[0]
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection", lambda: functions_result[1]
    )
    assert can_access_google_page("") == response
