import pytest
from unittest import mock
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,status,internet,result",
    [
        ("google.com", True, False, "Not accessible"),
        ("google.com", True, True, "Accessible"),
        ("bing.com", False, False, "Not accessible"),
        ("bing.com", False, True, "Not accessible")
    ],
    ids=[
        "test_valid_url_night_time",
        "test_valid_url_day_time",
        "test_non_valid_url_night_time",
        "test_non_valid_url_day_time"
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_access_google_page(
        mocked_has_internet_connection: mock,
        mocked_valid_google_url: mock,
        url: str,
        status: bool,
        internet: bool,
        result: str
) -> None:
    mocked_valid_google_url.return_value = status
    mocked_has_internet_connection.return_value = internet

    assert can_access_google_page(url) == result
