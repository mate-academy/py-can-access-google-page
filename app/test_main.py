from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mocked_connection_return_value, mocked_url_return_value, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "test_valid_url_and_connection",
        "test_not_valid_url",
        "test_has_not_connection",
        "test_not_valid_url_and_has_not_connection"
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection(
        mocked_connection: mock,
        mocked_url: mock,
        mocked_connection_return_value: bool,
        mocked_url_return_value: bool,
        result: str
) -> None:
    mocked_url.return_value = mocked_url_return_value
    mocked_connection.return_value = mocked_connection_return_value
    assert can_access_google_page("http:/google.com") == result
