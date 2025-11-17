import pytest
from typing import Callable
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet, url_valid, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_conn: Callable,
        mock_valid: Callable,
        internet: bool,
        url_valid: bool,
        expected: str
) -> None:
    mock_conn.return_value = internet
    mock_valid.return_value = url_valid

    result = can_access_google_page("https://example.com/")

    assert result == expected
    mock_conn.assert_called_once()

    if internet:
        mock_valid.assert_called_once_with("https://example.com/")
    else:
        mock_valid.assert_not_called()
