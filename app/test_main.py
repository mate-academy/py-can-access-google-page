import pytest
from typing import Callable

from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url ,has_internet_connection ,expected_result",
    [
        pytest.param(
            False,
            False,
            "Not accessible",
            id="Test only False"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Test False connection"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Test when not valid URL"
        ),
        pytest.param(
            True,
            True,
            "Accessible",
            id="Test only True"
        ),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_valid_url_and_connection(
        mock_valid_url: Callable,
        mock_connection: Callable,
        valid_google_url: bool,
        has_internet_connection: bool,
        expected_result: str
) -> None:
    mock_valid_url.return_value = valid_google_url
    mock_connection.return_value = has_internet_connection
    assert can_access_google_page(
        "https://www.google.com"
    ) == expected_result
