from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize("internet_connection, valid_url, expected_result", [
    (True, True, "Accessible"),
    (False, True, "Not accessible"),
    (True, False, "Not accessible"),
    (False, False, "Not accessible"),
])
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock,
        internet_connection: bool,
        valid_url: bool,
        expected_result: str
) -> None:

    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = valid_url

    result = can_access_google_page("https://www.google.com/")

    assert result == expected_result
