from unittest import mock
from unittest.mock import Mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_google_url,is_internet_connection_accessible,expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_valid_google: Mock,
                                mock_has_internet_connection: Mock,
                                is_valid_google_url: bool,
                                is_internet_connection_accessible: bool,
                                expected: str) -> None:
    mock_valid_google.return_value = is_valid_google_url
    mock_has_internet_connection.return_value =\
        is_internet_connection_accessible
    assert can_access_google_page("http://google.com") == expected
