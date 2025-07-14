from unittest.mock import patch, Mock

import pytest

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_should_call_valid_google_url_and_has_internet_connection(
        mocked_internet_connection: Mock,
        mocked_google_url: Mock
) -> None:
    can_access_google_page("https://www.google.com")
    mocked_internet_connection.assert_called_once()
    mocked_google_url.assert_called_once_with("https://www.google.com")


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    """url,valid_google_url_result,
    has_internet_connection_result,expected_result""",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.googl.com", False, True, "Not accessible"),
        ("https://www.googl.com", False, False, "Not accessible"),
    ]
)
def test_should_return_correct_result(
        mocked_internet_connection: Mock,
        mocked_google_url: Mock,
        url: str,
        valid_google_url_result: bool,
        has_internet_connection_result: bool,
        expected_result: str
) -> None:
    mocked_internet_connection.return_value = has_internet_connection_result
    mocked_google_url.return_value = valid_google_url_result
    assert can_access_google_page(url) == expected_result
