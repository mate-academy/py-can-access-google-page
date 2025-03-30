import pytest

from app.main import can_access_google_page
from unittest.mock import patch


@pytest.mark.parametrize(
    "internet_connection, valid_url, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        internet_connection: bool,
        valid_url: bool,
        expected_result: str
) -> None:

    with patch(
            "app.main.has_internet_connection",
            return_value=internet_connection
    ):
        with patch("app.main.valid_google_url", return_value=valid_url):
            result = can_access_google_page("http://www.google.com")
            assert result == expected_result
