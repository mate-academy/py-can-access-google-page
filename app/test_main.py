from unittest import mock

import pytest

from .main import can_access_google_page


@pytest.mark.parametrize(
    "status,internet,result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ],
    ids=[
        "test is not accessible, url is valid but disconnected",
        "test is not accessible, url is connected but invalid",
        "test is not accessible, url is invalid and disconnected",
        "test is accessible, url is valid and connected"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google(
        mocked_internet: mock,
        mocked_google: mock,
        status: bool,
        internet: bool,
        result: str
) -> None:
    url = "google.com"
    mocked_google.return_value = status
    mocked_internet.return_value = internet

    assert can_access_google_page(url) == result
