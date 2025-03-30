from app.main import can_access_google_page
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "link_available, internet_connection, is_successful",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_getting_access_to_the_page(mocked_valid_google_url: mock,
                                    mocked_availability_to_internet: mock,
                                    is_successful: str,
                                    internet_connection: bool,
                                    link_available: bool) -> None:
    mocked_availability_to_internet.return_value = internet_connection
    mocked_valid_google_url.return_value = link_available
    assert can_access_google_page("https://mate.academy/") == is_successful
