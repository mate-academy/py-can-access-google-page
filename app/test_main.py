import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connected, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "has_internet_connection_and_valid_url",
        "has_internet_connection_and_invalid_url",
        "hasn't_internet_connection_and_valid_url",
        "hasn't_internet_connection_and_invalid_url"
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(mocked_url: mock.Mock,
                                         mocked_internet_connection: mock.Mock,
                                         valid_url: bool,
                                         internet_connected: bool,
                                         expected: str
                                         ) -> None:
    """Test can_access_google_page with different internet and URL conditions.

        Args:
            mocked_internet: Mock for has_internet_connection
            mocked_url: Mock for valid_google_url
            internet_connected: Simulated internet status
            url_valid: Simulated URL validity
            expected: Expected result string
    """

    mocked_url.return_value = valid_url  # Mock the `valid_google_url` function
    mocked_internet_connection.return_value = internet_connected  # Mock the

    # Checking whether the function returns the expected result
    assert can_access_google_page("https://www.google.com") == expected
