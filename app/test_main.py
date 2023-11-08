import pytest

from unittest import mock
from unittest.mock import Mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, connection, expected", [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_url: Mock,
        mock_connect: Mock,
        url: bool,
        connection: bool,
        expected: str
) -> None:
    mock_connect.return_value = connection
    mock_valid_url.return_value = url
    assert can_access_google_page("www.google.com") == expected
