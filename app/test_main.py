import datetime
import pytest
from unittest import mock
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
        valid_google_url,
        expected
):
    with mock.patch("app.main.has_internet_connection") as mocked_datatime:
        mocked_datatime.now.return_value = current_time

        with mock.patch(
                "app.main.valid_google_url",
                return_value=valid_google_url
        ):
            result = main.can_access_google_page("https://www.google.com")
    assert result == expected
