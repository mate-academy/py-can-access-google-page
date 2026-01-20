import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "check_connect, valid_url, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_connection: mock,
        mocked_valid_url: mock,
        check_connect: bool,
        valid_url: bool,
        expected_result: str
) -> None:
    mocked_connection.return_value = check_connect
    mocked_valid_url.return_value = valid_url

    assert can_access_google_page("https://www.google.com") == expected_result
