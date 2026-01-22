from unittest import mock
import pytest

from app.main import can_access_google_page


URL = "https://www.google.com"


@pytest.mark.parametrize(
    "res_valid_google_url, res_internet_connection, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Should return 'Accessible' when all functions = True",
        "Should return 'Not accessible' when res_valid_google_url = False",
        "Should return 'Not accessible' when res_internet_connection = False",
        "Should return 'Not accessible' when all functions = False",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mock_has_internet_connection,
        mock_valid_google_url,
        res_valid_google_url,
        res_internet_connection,
        expected
):
    mock_valid_google_url.return_value = res_valid_google_url
    mock_has_internet_connection.return_value = res_internet_connection

    assert can_access_google_page(URL) == expected
