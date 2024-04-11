from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page

import pytest


@pytest.mark.parametrize(
    "url, expected_result, mocked_hour",
    [
        ("", "Not accessible", 5),
        ("hsgdfjhg", "Not accessible", 2),
        ("http://www.google.com", "Accessible", 18),
        ("http://www.google.com", "Not accessible", 4),
        ("https://www.gogle.com", "Not accessible", 23),
    ]
)
def test_can_access_google_page_get_expected_value(
        url: str,
        expected_result: str,
        mocked_hour: int
) -> None:
    with mock.patch("app.main.datetime.datetime") as mocked_datetime:
        mocked_now = mock.Mock()
        mocked_now.hour = mocked_hour
        mocked_datetime.now.return_value = mocked_now
        assert can_access_google_page(url) == expected_result


def test_has_internet_connection_and_can_access_google_page_was_called(
) -> None:
    with mock.patch(
        "app.main.has_internet_connection"
    ) as mocked_has_connection, mock.patch(
        "app.main.valid_google_url"
    ) as mocked_valid_url:

        url = "https://www.google.com"
        can_access_google_page(url)
        mocked_has_connection.assert_called_once()
        mocked_valid_url.assert_called_once()
