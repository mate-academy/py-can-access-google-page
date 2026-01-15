from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "internet_connection_value,valid_url_value,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible")
    ],
    ids=[
        "should return 'Accessible' when url is valid and has internet connection",
        "should return 'Not accessible' when url is not valid",
        "should return 'Not accessible' when has no internet connection",
        "should return 'Not accessible' when url is not valid and has no internet connection",
    ]
)
def test_can_access_google_page(internet_connection_value, valid_url_value, expected_result):
    with mock.patch('app.main.has_internet_connection') as mock_internet_connection:
        with mock.patch('app.main.valid_google_url') as mock_valid_url:
            mock_internet_connection.return_value = internet_connection_value
            mock_valid_url.return_value = valid_url_value
            assert can_access_google_page('url') == expected_result
