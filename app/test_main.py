from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_google_url: MagicMock,
                                mock_has_internet_conn: MagicMock,
                                valid_google_url: bool,
                                has_internet_connection: bool,
                                result: str) -> None:
    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet_conn.return_value = has_internet_connection
    url = "qweqwe.com"
    assert can_access_google_page(url) == result
