from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection,valid_url,expected",
    [
        pytest.param(True,
                     True,
                     "Accessible",
                     id="everything is valid"),
        pytest.param(True,
                     False,
                     "Not accessible",
                     id="url isn't valid"),
        pytest.param(False,
                     True,
                     "Not accessible",
                     id="internet connection isn't valid"),
        pytest.param(False,
                     False,
                     "Not accessible",
                     id="nothing is valid"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_url,
                                mock_internet_connection,
                                internet_connection,
                                valid_url,
                                expected):
    mock_valid_url.return_value = valid_url
    mock_internet_connection.return_value = internet_connection
    assert can_access_google_page("google.com") == expected
