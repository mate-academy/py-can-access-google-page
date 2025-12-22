import pytest
from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mocked_has_internet_connection: mock.MagicMock,
        mocked_valid_google_url: mock.MagicMock
) -> None:
    can_access_google_page("url")
    mocked_has_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once_with("url")


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "internet_connection, google_url, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ])
def test_correct_access(
        mocked_has_internet_connection: mock.MagicMock,
        mocked_valid_google_url: mock.MagicMock,
        internet_connection: bool,
        google_url: bool,
        expected_result: str,
) -> None:
    mocked_has_internet_connection.return_value = internet_connection
    mocked_valid_google_url.return_value = google_url
    result = can_access_google_page("url")
    assert result == expected_result
