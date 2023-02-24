from app.main import can_access_google_page
from unittest import mock
import pytest


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "validate_google_url, has_internet_connection, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "validate_url True, internet_connection True",
        "validate_url True, internet_connection False",
        "validate_url False, internet_connection True",
        "validate_url False, internet_connection False"
    ]

)
def test_can_access_google_page(
        mock_validate_google_url: mock.Mock,
        mock_has_internet_connection: mock.Mock,
        validate_google_url: bool,
        has_internet_connection: bool,
        expected_result: str
) -> None:
    mock_validate_google_url.return_value = validate_google_url
    mock_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page("https://www.google.com/") == expected_result
