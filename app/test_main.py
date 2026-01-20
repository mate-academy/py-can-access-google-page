import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, valid_url, expected_message",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
    ],
    ids=["positive_scenario", "negative_scenario"]
)
def test_can_access_google_page_positive_negative(
        internet_connection: bool,
        valid_url: bool,
        expected_message: str,
) -> None:
    with (mock.patch("app.main.has_internet_connection") as
          mocked_internet_connection,
          mock.patch("app.main.valid_google_url") as
          mocked_valid_url):
        mocked_internet_connection.return_value = internet_connection
        mocked_valid_url.return_value = valid_url
        assert can_access_google_page("url") == expected_message


@pytest.mark.parametrize(
    "internet_connection, valid_url, expected_message",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
    ],
    ids=["invalid_url", "no_internet_connection"]
)
def test_can_access_google_page_negative(
        internet_connection: bool,
        valid_url: bool,
        expected_message: str,
) -> None:
    with (mock.patch("app.main.has_internet_connection") as
          mocked_internet_connection,
          mock.patch("app.main.valid_google_url") as
          mocked_valid_url):
        mocked_internet_connection.return_value = internet_connection
        mocked_valid_url.return_value = valid_url
        assert can_access_google_page("url") == expected_message
