import pytest


from app.main import can_access_google_page


@pytest.mark.parametrize("url_valid,has_connection,expected", [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible")
])
def test_can_accessible(
        url_valid: bool,
        has_connection: bool,
        expected: str,
        mocker: object
) -> None:
    mocker.patch("app.main.valid_google_url", return_value=url_valid)
    mocker.patch(
        "app.main.has_internet_connection",
        return_value=has_connection
    )

    result = can_access_google_page("https://google.com")
    assert result == expected
