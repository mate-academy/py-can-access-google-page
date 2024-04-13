import pytest
from typing import Any
from unittest import mock


import app.main


@pytest.mark.parametrize(
    ("return_value_url", "return_value_connection", "url", "assert_response"),
    [
        pytest.param(
            True, True, "google.com", "Accessible",
            id="test should return Accessible when everything is correct"
        ),
        pytest.param(
            False, True, "google..com", "Not accessible",
            id="test should return Not accessible when url is wrong"
        ),
        pytest.param(
            True, False, "google.com", "Not accessible",
            id="test should return Not accessible when connection is invalid"
        )
    ]
)
def test_check_all_outcomes(
        return_value_url: Any,
        return_value_connection: Any,
        url: Any,
        assert_response: Any
) -> None:
    with mock.patch("app.main.valid_google_url") as mock_url, \
            mock.patch("app.main.has_internet_connection") as mock_connection:
        mock_url.return_value = return_value_url
        mock_connection.return_value = return_value_connection
        assert app.main.can_access_google_page(url) == assert_response
        mock_connection.assert_called_once()
        if mock_connection.return_value is True:
            mock_url.assert_called_once_with(url)
