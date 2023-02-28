import pytest

from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection,is_valid_url,expected_access",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock,
        has_connection: bool,
        is_valid_url: bool,
        expected_access: str
) -> None:
    mock_valid_google_url.return_value = is_valid_url
    mock_has_internet_connection.return_value = has_connection
    assert can_access_google_page("https://www.google.com") == expected_access
