from unittest import mock

import pytest

from .main import can_access_google_page


@pytest.mark.parametrize(
    "url,status,internet,result",
    [
        ("google.com", True, False, "Not accessible"),
        ("gooogle.com", False, True, "Not accessible"),
        ("google.com", True, True, "Accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_google_page(
        mocked_internet: mock,
        mocked_google_url: mock,
        url: str,
        status: bool,
        internet: bool,
        result: str
) -> None:
    mocked_google_url.return_value = status
    mocked_internet.return_value = internet

    assert can_access_google_page(url) == result
