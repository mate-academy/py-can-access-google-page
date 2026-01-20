from unittest import mock

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "url_validity_value,internet_connection_value,expected_output",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="should return 'Accessible' when both valid_google_url() "
               "and has_internet_connection() return `True`",
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="should return 'Not accessible' when "
               "valid_google_url() returns `False`",
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="should return 'Not accessible' when "
               "has_internet_connection() returns `False`",
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="should return 'Not accessible' when both valid_google_url() "
               "and has_internet_connection() return `False`",
        ),
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
