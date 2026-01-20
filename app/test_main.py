from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid, has_internet, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock,
        is_valid: bool,
        has_internet: bool,
        result: str) -> None:
    mock_valid_google_url.return_value = is_valid
    mock_has_internet_connection.return_value = has_internet
    assert can_access_google_page("https://google.com") == result
