from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "good link and good internet connection",
        "good link but no internet connection",
        "bad link but good internet connection",
        "ban link and no internet connection"
    ]
)
def test_can_access_google_page(valid_google_url: bool,
                                has_internet_connection: bool,
                                result: str) -> None:
    with (
        mock.patch("app.main.valid_google_url") as mocked_link,
        mock.patch("app.main.has_internet_connection") as mocked_connection
    ):
        mocked_link.return_value = valid_google_url
        mocked_connection.return_value = has_internet_connection
        assert can_access_google_page("http://google.com") == result
