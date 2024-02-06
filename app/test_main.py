from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "testing_connection,testing_url,expected",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="have internet connection and valid url",
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="have internet connection but invalid url",
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="no internet connection but valid url",
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="no internet connection and invalid url",
        ),
    ]
)
@mock.patch('app.main.valid_google_url')
@mock.patch('app.main.has_internet_connection')
def test_can_access_google_page(
        mocked_internet_connection,
        mocked_valid_url,
        testing_connection,
        testing_url,
        expected
):
    mocked_internet_connection.return_value = testing_connection
    mocked_valid_url.return_value = testing_url
    assert can_access_google_page("") == expected
