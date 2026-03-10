from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize("url, connection, expected_results", [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible")
])
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_google_access(
        mock_valid_google_url,
        mock_has_internet_connection,
        url,
        connection,
        expected_results
) -> None:
    mock_valid_google_url.return_value = url
    mock_has_internet_connection.return_value = connection
    assert can_access_google_page("") == expected_results
