from unittest.mock import patch, MagicMock

import pytest

from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
def test_has_internet_connection_was_called(mocked_func: MagicMock) -> None:
    can_access_google_page("http://www.google.com.ua/")
    mocked_func.assert_called_once()


@patch("app.main.valid_google_url")
def test_valid_google_url_was_called(mocked_func: MagicMock) -> None:
    can_access_google_page("http://www.google.com.ua/")
    mocked_func.assert_called_once_with("http://www.google.com.ua/")


@pytest.mark.parametrize(
    "valid_url,internet_connection,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_should_return_expected_result(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock,
        valid_url: bool,
        internet_connection: bool,
        expected_result: str) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("https://www.google.com") == expected_result
