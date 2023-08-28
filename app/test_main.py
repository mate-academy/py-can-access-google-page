import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "functions_result, response",
    [
        ([True, True], "Accessible"),
        ([False, True], "Not accessible"),
        ([True, False], "Not accessible"),
    ],
)
def test_can_access_google_page_with_different_url_and_connection_status(
        functions_result: list[bool], response: str
) -> None:
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(
        "app.main.valid_google_url",
        lambda *args: functions_result[0]
    )
    monkeypatch.setattr(
        "app.main.has_internet_connection",
        lambda: functions_result[1]
    )
    assert can_access_google_page("") == response
