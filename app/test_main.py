import pytest
from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "url,expected_result,internet_connection_value,valid_url_value",
    [
        pytest.param(
            "https://www.google.com",
            "Accessible",
            True,
            True,
            id=("return 'Accessible' if has internet "
                "connection and url is valid")
        ),
        pytest.param(
            "https://www.google.com",
            "Not accessible",
            True,
            False,
            id=("return 'Not accessible' if has internet "
                "connection and url is NOT valid")
        ),
        pytest.param(
            "https://www.google.com",
            "Not accessible",
            False,
            True,
            id=("return 'Not accessible' if has NOT internet "
                "connection and url is valid")
        )

    ]
)
def test_can_access_google_page(mock_valid_google_url: Callable,
                                mock_has_internet_connection: Callable,
                                url: str,
                                expected_result: str,
                                internet_connection_value: bool,
                                valid_url_value: bool) -> None:
    mock_has_internet_connection.return_value = internet_connection_value
    mock_valid_google_url.return_value = valid_url_value
    assert can_access_google_page(url) == expected_result
