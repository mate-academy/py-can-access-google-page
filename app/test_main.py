from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connect_value,valid_value,result",
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
        mocked_connection,
        mocked_valid_url,
        connect_value: bool,
        valid_value: bool,
        result: str
) -> None:
    url = "https://docs.python.org/3/library/unittest.mock.html"
    mocked_connection.return_value = connect_value
    mocked_valid_url.return_value = valid_value
    assert can_access_google_page(url) == result