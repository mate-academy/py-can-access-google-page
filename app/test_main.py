from unittest.mock import patch
import pytest
from app.main import can_access_google_page

url = "https://www.notavalidurl.com"


@pytest.mark.parametrize("internet_connection, valid_url, expected_result", [
    (True, True, "The Google page is accessible."),
    (False, True, "The Google page is not accessible "
                  "due to lack of internet connection."),
    (True, False, "The provided URL is not a valid Google URL."),
    (False, False, "The Google page is not accessible "
                   "due to lack of internet connection "
                   "and the provided URL is not a valid Google URL.")
])
def test_can_access_google_page(internet_connection: bool,
                                valid_url: bool,
                                expected_result: str) -> None:
    with patch("app.main.has_internet_connection",
               return_value=internet_connection):
        with patch("app.main.valid_google_url",
                   return_value=valid_url):
            assert can_access_google_page(url) == expected_result
