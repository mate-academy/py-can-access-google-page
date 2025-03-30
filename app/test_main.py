from pytest import mark, param, MonkeyPatch

from app.main import can_access_google_page


@mark.parametrize(
    "validation, connection, expected_result",
    [
        param(
            True, True, "Accessible",
            id="Access to the page if all requirements are followed"),
        param(
            False, True, "Not accessible",
            id="The page cannot be opened if the URL is incorrect"),
        param(
            True, False, "Not accessible",
            id="The page cannot be accessed if no Internet connection"),
        param(
            False, False, "Not accessible",
            id="The page cannot be accessed if all requirements are failed"),
    ]
)
def test_can_access_google_page(
    validation: bool,
    connection: bool,
    expected_result: str,
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda val: validation)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: connection)

    assert can_access_google_page("test url") == expected_result
