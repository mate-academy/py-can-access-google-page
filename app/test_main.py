import datetime
from unittest import mock

import pytest

from app import main


@pytest.mark.parametrize(
    "current_time, valid_google_url, expected",
    [
        (
            datetime.datetime(2024, 1, 1, 5, 59, 59),
            True,
            "Not accessible",
        ),
        (
            datetime.datetime(2024, 1, 1, 6, 0, 0),
            True,
            "Accessible"
        ),
        (
            datetime.datetime(2024, 1, 1, 22, 59, 59),
            True,
            "Accessible"
        ),
        (
            datetime.datetime(2024, 1, 1, 23, 0, 0),
            True,
            "Not accessible"
        ),
        (
            datetime.datetime(2024, 1, 1, 12, 0, 0),
            False,
            "Not accessible"
        )
    ]
)
def test_can_access_google_page(
        current_time: datetime.datetime,
        valid_google_url: bool,
        expected: str
):
    with mock.patch("app.main.datetime.datetime") as mocked_datetime:
        mocked_datetime.now.return_value = current_time

        with mock.patch(
                "app.main.valid_google_url",
                return_value=valid_google_url
        ):
            result = main.can_access_google_page("https://www.google.com")
    assert result == expected
