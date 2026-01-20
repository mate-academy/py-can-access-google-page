import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection, valid_url, expected_result",
    [
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_function_can_access_google_page(
        mocked_connection: mock.Mock,
        mocked_url: mock.Mock,
        connection: bool,
        valid_url: bool,
        expected_result: str
) -> None:
    mocked_connection.return_value = connection
    mocked_url.return_value = valid_url
    assert can_access_google_page("https://www.google.com/") == expected_result
