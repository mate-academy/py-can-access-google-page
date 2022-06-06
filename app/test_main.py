import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection,valid_url,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_of_google_page(
        mocked_internet_connection,
        mocked_valid_url,
        internet_connection,
        valid_url,
        result
):
    mocked_internet_connection.return_value = internet_connection
    mocked_valid_url.return_value = valid_url

    assert can_access_google_page("mate.ua") == result
