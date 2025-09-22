from unittest import mock
from unittest.mock import MagicMock

import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_google_url, is_has_internet_connection, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_google_url(
        mock_has_internet_connection : MagicMock,
        mock_valid_google_url : MagicMock,
        is_valid_google_url : bool,
        is_has_internet_connection : bool,
        expected_result : str
) -> None:
    mock_valid_google_url.return_value = is_valid_google_url
    mock_has_internet_connection.return_value = is_has_internet_connection
    assert can_access_google_page("https://google.com") == expected_result
