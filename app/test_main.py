import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid, has_connection, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "URL is valid and there is connection",
        "URL is valid, but no connection",
        "URL is invalid, but we have connection",
        "URL is invalid and no internet connection",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_connection: callable,
                                mock_validator: callable,
                                is_valid: bool,
                                has_connection: bool,
                                result: str) -> None:
    mock_validator.return_value = is_valid
    mock_connection.return_value = has_connection
    assert can_access_google_page("https://www.google.com") == result
