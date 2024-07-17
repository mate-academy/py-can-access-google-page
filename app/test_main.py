from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,url_validity,has_internet_connection,expected_result",
    [
        ("https://mate.academy/", True, True, "Accessible"),
        ("https://mate.academy/", True, False, "Not accessible"),
        ("https://mate.academy123/", False, True, "Not accessible"),
        ("https://mate.academy123/", False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        url: str,
        url_validity: bool,
        has_internet_connection: bool,
        expected_result: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mock_valid_google_url,
        mock.patch("app.main.has_internet_connection") as mock_has_connection
    ):
        mock_valid_google_url.return_value = url_validity
        mock_has_connection.return_value = has_internet_connection

    assert can_access_google_page(url) == expected_result
