import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection_result,valid_google_url_result,result",
    [
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (True, True, "Accessible"),
    ],
)
def test_can_access_google_page(
        has_internet_connection_result: bool,
        valid_google_url_result: bool,
        result: str) -> None:
    with mock.patch("app.main.has_internet_connection") as inet_connection:
        with mock.patch("app.main.valid_google_url") as valid_google_url:
            valid_google_url.return_value = valid_google_url_result
            inet_connection.return_value = has_internet_connection_result
            assert (
                can_access_google_page("https://www.google.com") == result
            )
