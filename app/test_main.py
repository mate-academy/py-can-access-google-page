import pytest
from app.main import can_access_google_page
from unittest import mock


@pytest.mark.parametrize(
    "has_internet_connection_return,"
    "valid_google_url_return,"
    "expected_output",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_has_internet_connection: mock,
        mock_valid_google_url: mock,
        has_internet_connection_return: bool,
        valid_google_url_return: bool,
        expected_output: str
) -> None:
    mock_has_internet_connection.return_value = has_internet_connection_return
    mock_valid_google_url.return_value = valid_google_url_return
    assert can_access_google_page("https://www.google.com/") == expected_output
