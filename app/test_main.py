# flake8: noqa: *
from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_return,internet_return,expected_result", [
        pytest.param(True, True, "Accessible", id="All func return True"),
        pytest.param(False, True, "Not accessible", id="Valid False"),
        pytest.param(True, False, "Not accessible", id="Internet connection False"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(mock_valid, mock_internet_connection, valid_return, internet_return, expected_result):
    mock_valid.return_value = valid_return
    mock_internet_connection.return_value = internet_return
    assert can_access_google_page("random url") == expected_result
