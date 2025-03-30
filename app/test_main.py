from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection,url,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_google_url: mock.Mock,
        mocked_has_internet_connection: mock.Mock,
        connection: bool,
        url: bool,
        expected_result: str
) -> None:
    mocked_valid_google_url.return_value = url
    mocked_has_internet_connection.return_value = connection
    assert can_access_google_page("https://www.google.com/") == expected_result
