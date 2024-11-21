import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection,valid_google_url,expected",
    [
        pytest.param(
            True, True, "Accessible",
            id="Accessible if internet connection and url is valid"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="Not accessible if no internet connection"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="Not accessible if url is not valid"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="Not accessible if no internet connection and url is not valid"
        )
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_internet_connection,
        mocked_valid_google_url,
        has_internet_connection,
        valid_google_url,
        expected
):
    mocked_internet_connection.return_value = has_internet_connection
    mocked_valid_google_url.return_value = valid_google_url

    assert can_access_google_page("https://google.com/") == expected
