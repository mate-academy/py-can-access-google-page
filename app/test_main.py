from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url,has_internet_connection,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]

)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_google_url: mock,
        mocked_has_internet_connection: mock,
        valid_google_url: bool,
        has_internet_connection: bool,
        result: str) -> None:
    mocked_valid_google_url.return_value = valid_google_url
    mocked_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page("https://www.wikipedia.org") == result
