from unittest.mock import patch, Mock
from pytest import mark
from app.main import can_access_google_page


@mark.parametrize(
    "input_url, output_validator, connection_status, expected_result",
    [
        ("https://www.google.com/", True, True, "Accessible"),
        ("httpswww.google.co", False, True, "Not accessible"),
        ("https://www.google.com/", True, False, "Not accessible"),
        ("httpswww.google.co", False, False, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_internet_connection: Mock,
        mocked_validator: Mock,
        input_url: str,
        output_validator: bool,
        connection_status: bool,
        expected_result: str
) -> None:
    mocked_internet_connection.return_value = connection_status
    mocked_validator.return_value = output_validator
    assert can_access_google_page(input_url) == expected_result
