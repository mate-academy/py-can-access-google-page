import pytest
from unittest import mock
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_connection, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        # mock_url_page,
        mock_has_internet_connection: mock,
        mock_valid_google_url: mock,
        valid_url: bool,
        has_connection: bool,
        expected: str
) -> None:
    # Mocking the functions
    mock_has_internet_connection.return_value = has_connection
    mock_valid_google_url.return_value = valid_url

    assert can_access_google_page("https://google.com/") == expected
