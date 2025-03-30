from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,internet_access,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "Certain URL, with Internet: Accessible",
        "Certain URL, without Internet: Not accessible",
        "Invalid URL, with Internet: Not accessible",
        "Invalid URL, without Internet: Not accessible"
    ]
)
def test_can_access_google_page(
        valid_url: bool,
        internet_access: bool,
        result: str
) -> None:
    with (mock.patch("app.main.valid_google_url",
                     lambda *args: valid_url),
          mock.patch("app.main.has_internet_connection",
                     lambda *args: internet_access)):
        assert can_access_google_page("url") == result
