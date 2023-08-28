import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, expected_output",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "should return 'Accessible' if url and internet connection is True",
        "should return 'Not accessible' if url not valid",
        "should return 'Not accessible' if no internet connection",
        "should return 'Not accessible' if all False"
    ]
)
def test_can_access_google_page(
    valid_url: bool,
    internet_connection: bool,
    expected_output: str
) -> None:
    with (
        mock.patch("app.main.valid_google_url")
        as mock_valid_google_url,
        mock.patch("app.main.has_internet_connection")
        as mock_has_internet_connection
    ):
        mock_valid_google_url.return_value = valid_url
        mock_has_internet_connection.return_value = internet_connection
        assert can_access_google_page("google.com") == expected_output
