import pytest

from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "is_valid,is_connected,result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Accessible when connected to internet and url is valid",
        "Not accessible when connected to internet and url is invalid",
        "Not accessible when not connected to internet and url is valid",
        "Not accessible when not connected to internet and url is invalid",
    ]
)
def test_can_access_google_page(
        mocked_valid_google_url: object,
        mocked_has_internet_connection: object,
        is_valid: bool,
        is_connected: bool,
        result: str,
) -> None:
    mocked_valid_google_url.return_value = is_valid
    mocked_has_internet_connection.return_value = is_connected
    assert can_access_google_page("") == result
