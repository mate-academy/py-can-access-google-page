from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, exists, internet, result",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://some_example.com", False, True, "Not accessible"),
    ]
)
def test_is_valid_url_and_internet(
        url: str,
        exists: bool,
        internet: bool,
        result: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url", return_value=exists),
        mock.patch("app.main.has_internet_connection", return_value=internet)
    ):
        assert can_access_google_page(url) == result
