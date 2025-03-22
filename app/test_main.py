import pytest
from app.main import can_access_google_page
from unittest import mock


@pytest.fixture()
def mocked_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_test_response:
        yield mock_test_response


@pytest.fixture()
def mocked_has_internet_connection() -> None:
    with (mock.patch("app.main.has_internet_connection")
          as mock_test_current_time):
        yield mock_test_current_time


def test_can_access_google_page_when_valid_url_and_connection(
        mocked_valid_google_url: bool,
        mocked_has_internet_connection: bool
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"

    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False
    result = can_access_google_page("https://www.google.com/")
    assert result == "Not accessible"
    mocked_valid_google_url.assert_called_with("https://www.google.com")
    mocked_has_internet_connection.assert_called()

    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False
    result = can_access_google_page("https://www.google.com/")
    assert result == "Not accessible"
    mocked_valid_google_url.assert_called_with("https://www.google.com")
    mocked_has_internet_connection.assert_called()

# write your code here
