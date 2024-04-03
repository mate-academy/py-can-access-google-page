from unittest.mock import MagicMock, patch

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_connection, expected_output",
    [
        pytest.param(True, True, "Accessible",
                     id="valid_url_with_connection"),
        pytest.param(True, False, "Not accessible",
                     id="valid_url_no_connection"),
        pytest.param(False, True, "Not accessible",
                     id="invalid_url_with_connection"),
        pytest.param(False, False, "Not accessible",
                     id="invalid_url_no_connection"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_cannot_access_if_connection_or_valid_url_is_true(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock,
        valid_url: bool,
        has_connection: bool,
        expected_output: str
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_connection

    result = can_access_google_page("https://www.google.com/")

    mock_valid_google_url.assert_called_once()

    if valid_url:
        mock_has_internet_connection.assert_called_once()
    else:
        mock_has_internet_connection.assert_not_called()
    assert result == expected_output
