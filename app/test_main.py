from app.main import can_access_google_page
import pytest
import datetime
from unittest import mock


@pytest.mark.parametrize(
    "url_page,status_code,fake_datetime,expected",
    [
        ("https://googlecom", 404,
         datetime.datetime(2222, 2, 2, 6, 00, 00), "Not accessible"),
        ("https://www.google.com", 200,
         datetime.datetime(2222, 2, 2, 6, 00, 00), "Accessible"),
        ("https://www.google.com", 200,
         datetime.datetime(2222, 2, 2, 22, 59, 59), "Accessible"),
        ("https://www.google.com", 200,
         datetime.datetime(2222, 2, 2, 23, 00, 00), "Not accessible")
    ]
)
def test_can_access_google_page(url_page: str,
                                status_code: int,
                                fake_datetime: datetime.datetime,
                                expected: str) -> None:
    with mock.patch("app.main.valid_google_url") as mock_requests:
        mock_requests.get.return_value.status_code = status_code
        with mock.patch("app.main.has_internet_connection") as mock_datetime:
            mock_datetime.datetime.now.return_value = fake_datetime
            assert can_access_google_page(url_page) == expected
