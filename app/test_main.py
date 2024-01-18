from unittest.mock import Mock, patch

from pytest import mark

from app.main import can_access_google_page


@mark.parametrize(
    "output_validator, connection_status, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_internet_connection: Mock,
        mocked_validator: Mock,
        output_validator: bool,
        connection_status: bool,
        expected_result: str
) -> None:
    mocked_internet_connection.return_value = connection_status
    mocked_validator.return_value = output_validator
    assert can_access_google_page("https://www.google.com/") == expected_result
