from unittest import mock

import datetime
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(

    "status, time, result",
    [
        (
            200, datetime.time(22, 0, 0), "Accessible"
        ),
        (
            200, datetime.time(6, 0, 0), "Accessible"
        ),
        (
            100, datetime.time(8, 0, 0), "Not accessible"
        ),
        (
            200, datetime.time(5, 0, 0), "Not accessible"
        ),
        (
            0, datetime.time(3, 0, 0), "Not accessible"
        )
    ]
)
@mock.patch("requests.get")
@mock.patch("datetime.datetime")
def test_access_google_page(
    mock_datetime: mock.Mock,
    mock_response: mock.Mock,
    status: int,
    time: datetime.time,
    result: str
) -> None:
    mock_response.return_value.status_code = status
    mock_datetime.now.return_value = time

    assert can_access_google_page("http://google.com") == result
