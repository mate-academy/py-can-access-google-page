import pytest
from unittest import mock
from unittest.mock import Mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, mocked_internet_return, mocked_valid_return, expected",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://google.com", True, False, "Not accessible"),
        ("https://google.com", False, True, "Not accessible"),
        ("https://google.com", False, False, "Not accessible"),
    ],
    ids=[
        "Accessible when URL is valid and internet is available",
        "Not accessible when URL is invalid and internet is available",
        "Not accessible when URL is invalid and internet is not available",
        "Not accessible when URL is invalid and internet is not available",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_internet: Mock,
        mocked_valid: Mock, url: str,
        mocked_internet_return: bool,
        mocked_valid_return: bool,
        expected: str
) -> None:
    mocked_internet.return_value = mocked_internet_return
    mocked_valid.return_value = mocked_valid_return

    assert can_access_google_page(url) == expected
