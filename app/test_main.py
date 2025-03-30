import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize("url, internet_connection, expected_result", [
    pytest.param("https://www.google.com", True,
                 "Accessible", id="Valid URL and internet connection"),
    pytest.param("https://www.google.com", False,
                 "Not accessible", id="Valid URL but no internet connection"),
    pytest.param("https://invalid-url.com", True,
                 "Not accessible", id="Invalid URL but internet connection"),
    pytest.param("https://invalid-url.com", False,
                 "Not accessible", id="Invalid URL and no connection"),
])
def test_can_access_google_page(
        url: str,
        internet_connection: bool,
        expected_result: str
) -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url, \
         mock.patch("app.main.has_internet_connection") as mocked_connection:

        mocked_url.return_value = url == "https://www.google.com"
        mocked_connection.return_value = internet_connection

        assert can_access_google_page(url) == expected_result
