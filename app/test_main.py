import pytest
from unittest import mock
from app.main import can_access_google_page
from unittest.mock import Mock


@pytest.mark.parametrize("has_internet_connection, valid_google_url, expected",
                         [(True, True, "Accessible"),
                          (True, False, "Not accessible"),
                          (False, True, "Not accessible"),
                          (False, False, "Not accessible")])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_main_can_access_google_page(mock_valid_google_url: Mock,
                                     mock_has_internet_connection: Mock,
                                     has_internet_connection: bool,
                                     valid_google_url: bool,
                                     expected: str) -> None:
    mock_has_internet_connection.return_value = has_internet_connection
    mock_valid_google_url.return_value = valid_google_url
    result = can_access_google_page("https://www.google.com")
    assert result == expected
