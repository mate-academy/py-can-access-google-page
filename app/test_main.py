import pytest
from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_result, url_result, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
    ],
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock,
        internet_result: bool,
        url_result: bool,
        expected: str,
) -> None:
    mock_has_internet_connection.return_value = internet_result
    mock_valid_google_url.return_value = url_result
    assert can_access_google_page("") == expected
