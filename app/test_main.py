import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url,has_internet_connection,expected_value",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Valid url and has internet",
        "Valid url but hasn't internet",
        "Invalid url but has internet",
        "Invalid url and hasn't internet",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock,
        valid_google_url: bool,
        has_internet_connection: bool,
        expected_value: str
) -> None:
    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page("https://www.google.com") == expected_value
