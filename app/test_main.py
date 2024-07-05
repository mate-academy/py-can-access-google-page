import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_connection, is_valid_url, is_accessible",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_is_access_being_obtained_correctly(
        mocked_has_internet_connection: mock,
        mocked_valid_google_url: mock,
        is_connection: bool,
        is_valid_url: bool,
        is_accessible: str
) -> None:
    mocked_has_internet_connection.return_value = is_connection
    mocked_valid_google_url.return_value = is_valid_url
    assert can_access_google_page("https://www.google.com/") == is_accessible
