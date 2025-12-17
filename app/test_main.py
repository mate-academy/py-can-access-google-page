from unittest.mock import patch

from typing import Any

import pytest

import app.main


@pytest.mark.parametrize(
    "internet_connection, valid_url, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_internet_connection: Any,
                                mock_valid_url: Any,
                                internet_connection: bool,
                                valid_url: bool,
                                result: str) -> str:
    mock_internet_connection.return_value = internet_connection
    mock_valid_url.return_value = valid_url
    test_results = app.main.can_access_google_page("some_url")
    assert test_results == result
    mock_internet_connection.assert_called_once()
    if internet_connection is True:
        mock_valid_url.assert_called_with("some_url")
    else:
        assert not mock_valid_url.called
