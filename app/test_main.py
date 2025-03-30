import pytest
from unittest import mock


from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "is_valid,internet_connection,expected_status",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "should not be accessible when there's no internet connection",

        "should be accessible when url isn't valid "
        "and user has internet connection",

        "should be accessible when url is valid "
        "and user has internet connection",

        "should not be accessible when url is not valid "
        "and there's no internet connection"
    ]
)
def test_accesses_pages_correctly(mocked_valid_url: mock.Mock,
                                  mocked_has_internet_connection: mock.Mock,
                                  is_valid: bool,
                                  internet_connection: bool,
                                  expected_status: str) -> None:
    mocked_valid_url.return_value = is_valid
    mocked_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("https://www.google.com") == expected_status
