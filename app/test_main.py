from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,internet_connection,access_page_status",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Page should be accessible if you have "
        "valid url and internet connection",
        "Page shouldn't be accessible if you haven't "
        "valid internet connection",
        "Page shouldn't be accessible if you haven't valid url",
        "Page shouldn't be accessible if you haven't "
        "both valid url and internet connection",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_url: mock.Mock,
        mocked_internet_connection: mock.Mock,
        valid_url: bool,
        internet_connection: bool,
        access_page_status: str
) -> None:
    mocked_valid_url.return_value = valid_url
    mocked_internet_connection.return_value = internet_connection
    assert can_access_google_page("some_url") == access_page_status
