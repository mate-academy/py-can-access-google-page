import pytest
from typing import Callable

from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url_return,internet_connection,expected_result",
    [
        pytest.param(False, False, "Not accessible", id="Test with two False"),
        pytest.param(True, False, "Not accessible", id="Test when connection False"),
        pytest.param(False, True, "Not accessible", id="Test when valid URL False"),
        pytest.param(True, True, "Accessible", id="Test with two True"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_for_the_correct_meaning_of_url_and_connection(
        mock_valid_url: Callable,
        mock_internet_connection: Callable,
        valid_url_return: bool,
        internet_connection: bool,
        expected_result: str
) -> None:
        mock_valid_url.return_value = valid_url_return
        mock_internet_connection.return_value = internet_connection
        assert can_access_google_page(
            "https://www.google.com"
        ) == expected_result
