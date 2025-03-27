from collections.abc import Callable
from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_status, is_url_valid, message",
    [
        pytest.param(True, True, "Accessible", id="valid data"),
        pytest.param(False, True, "Not accessible", id="no internet"),
        pytest.param(True, False, "Not accessible", id="wrong url")
    ])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access(mock_has_internet: Callable,
                    mock_valid_url: Callable,
                    internet_status: bool,
                    is_url_valid: bool,
                    message: str) -> None:
    mock_has_internet.return_value = internet_status
    mock_valid_url.return_value = is_url_valid
    result = can_access_google_page("https://www.google.com/")
    assert result == message
    mock_has_internet.assert_called_once()
    if internet_status:
        mock_valid_url.assert_called_once_with("https://www.google.com/")
