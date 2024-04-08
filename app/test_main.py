import pytest
from app.main import can_access_google_page
from unittest import mock


@pytest.mark.parametrize(
    "valid_google_url,has_internet_connection,expected_result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_has_internet_connection: mock,
        mocked_valid_google_url: mock,
        valid_google_url: bool,
        has_internet_connection: bool,
        expected_result: str
) -> None:
    mocked_valid_google_url.return_value = valid_google_url
    mocked_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page("https://www.google.com") == expected_result
