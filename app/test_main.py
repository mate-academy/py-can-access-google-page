from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "url, valid_url, has_connection, result",
    [
        ("https://www.google.com/", True, True, "Accessible"),
        ("https://www.google.con/", False, True, "Not accessible"),
        ("https://www.google.com/", True, False, "Not accessible"),
        ("https://www.google.con/", False, False, "Not accessible")

    ]
)
def test_can_access_google_page(
        url: str,
        valid_url: bool,
        has_connection: bool,
        result: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mock_valid_url,
        mock.patch("app.main.has_internet_connection") as mock_has_connection
    ):
        mock_valid_url.return_value = valid_url
        mock_has_connection.return_value = has_connection

        assert can_access_google_page(url) == result
