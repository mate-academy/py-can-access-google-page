from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_response,int_status,expected_value",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Response inet is status True",
        "Response True inet status False",
        "Response False inet status True",
        "Response False inet status False"
    ]
)
def test_can_access_google_page(
        url_response: bool,
        int_status: bool,
        expected_value: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url", return_value=url_response),
        mock.patch("app.main.has_internet_connection", return_value=int_status)
    ):
        assert can_access_google_page("https://google.com/") == expected_value
