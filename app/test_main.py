from pytest import mark, param, MonkeyPatch

from app.main import can_access_google_page


@mark.parametrize(
    "url, validation, connection, expected_result",
    [
        param(
            "https://www.google.com/", True, True, "Accessible",
            id="Access to the page if all requirements are followed"),
        param(
            "open google please", False, True, "Not accessible",
            id="The page cannot be opened if the URL is incorrect"),
        param(
            "https://www.google.com/", True, False, "Not accessible",
            id="The page cannot be accessed if no Internet connection"),
        param(
            "ok google, open google", False, False, "Not accessible",
            id="The page cannot be accessed if all requirements are failed"),
    ]
)
def test_can_access_google_page(
    url: str,
    validation: bool,
    connection: bool,
    expected_result: str,
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr("app.main.valid_google_url", lambda val: validation)
    monkeypatch.setattr("app.main.has_internet_connection", lambda: connection)

    assert can_access_google_page(url) == expected_result
