import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection_validator, url_validator, expected_value",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "Valid internet connection and Google server response",
        "Invalid internet connection",
        "Invalid the Google server response",
        "Invalid internet connection and Google server response"
    ]

)
def test_can_access_google_page(
        connection_validator: bool,
        url_validator: bool,
        expected_value: str
) -> None:
    with (
        mock.patch("app.main.has_internet_connection") as valid_connection,
        mock.patch("app.main.valid_google_url") as valid_url
    ):
        valid_connection.return_value = connection_validator
        valid_url.return_value = url_validator
        assert can_access_google_page(
            "https://www.google.com/"
        ) == expected_value
