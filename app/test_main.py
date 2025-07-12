from unittest.mock import patch

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_connection, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "valid url and has connection",
        "url is not valid",
        "no internet connection",
        "url is not valid and no internet connection"
    ]
)
def test_can_access_google_page_valid_url_and_has_connection(
        valid_url: bool,
        has_connection: bool,
        result: str
) -> None:
    with (
        patch("app.main.valid_google_url") as mocked_valid_url,
        patch("app.main.has_internet_connection") as mocked_connection
    ):
        mocked_valid_url.return_value = valid_url
        mocked_connection.return_value = has_connection
        assert can_access_google_page("http://example.com") == result
