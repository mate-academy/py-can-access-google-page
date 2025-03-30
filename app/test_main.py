import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_result,connection_result,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        url_result: bool,
        connection_result: bool,
        expected_result: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as valid_google_url,
        mock.patch("app.main.has_internet_connection")
        as has_internet_connection
    ):
        valid_google_url.return_value = url_result
        has_internet_connection.return_value = connection_result
        assert can_access_google_page("url") == expected_result
