from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,connection,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cannot_access_if_connection_or_valid_url_is_true(
        mocked_url: None,
        mocked_connection: None,
        url: bool,
        connection: bool,
        result: str
) -> None:
    mocked_url.return_value = url
    mocked_connection.return_value = connection
    assert can_access_google_page("http://mate.academy/") == result
