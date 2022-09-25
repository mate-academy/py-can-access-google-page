from unittest import mock

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "url_validity_value,internet_connection_value,expected_output",
    [
        pytest.param(True, True, "Accessible"),
        pytest.param(False, True, "Not accessible"),
        pytest.param(True, False, "Not accessible"),
        pytest.param(False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    mock_valid_url,
    mock_internet_connection,
    url_validity_value,
    internet_connection_value,
    expected_output,
):
    mock_valid_url.return_value = url_validity_value
    mock_internet_connection.return_value = internet_connection_value

    assert can_access_google_page("https://google.com") == expected_output
