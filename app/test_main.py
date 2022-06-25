from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "internet, url, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (True, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_internet, mocked_url,
                                internet, url, expected):
    mocked_internet.return_value = internet
    mocked_url.return_value = url
    assert can_access_google_page(url="") == expected
