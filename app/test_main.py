import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, internet_connection, expected_result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ]
)
def test_can_access_google_page(
        valid_google_url: bool,
        internet_connection: bool,
        expected_result: str
) -> None:
    with (mock.patch("app.main.has_internet_connection") as mocked_connect,
          mock.patch("app.main.valid_google_url") as mocked_url):
        mocked_connect.return_value = internet_connection
        mocked_url.return_value = valid_google_url
        assert can_access_google_page("https://www.google.com") == expected_result
