from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, exists, internet, result",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://some_example.com", False, True, "Not accessible"),
        ("https://google.com", True, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_is_valid_url_and_internet(
        moke_url: mock,
        moke_internet: mock,
        url: str,
        exists: bool,
        internet: bool,
        result: str
) -> None:
    moke_url.return_value = exists
    moke_internet.return_value = internet
    assert can_access_google_page(url) == result
