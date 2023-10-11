import datetime
import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize("url, date, result", [
    ("https://www.google.com/",
     datetime.datetime(2023, 10, 10, 10, 0, 0),
     "Accessible"),
    ("http://www.wed123.com/",
     datetime.datetime(2023, 10, 10, 10, 0, 0),
     "Not accessible"),
    ("https://www.google.com/",
     datetime.datetime(2023, 10, 10, 3, 0, 0),
     "Not accessible"),
    ("http://www.wed123.com/",
     datetime.datetime(2023, 10, 10, 3, 0, 0),
     "Not accessible")
])
def test_can_access_google_page_false(
        url: str,
        date: datetime,
        result: str
) -> None:
    with mock.patch("app.main.datetime.datetime") as mocked_datetime:
        mocked_datetime.now.return_value = date
        assert can_access_google_page(url) == result
