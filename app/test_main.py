from typing import Callable
from unittest import mock
from app.main import can_access_google_page

import pytest


@pytest.mark.parametrize(
    "url,valid_url,connection,result",
    [
        ("https://www.google.com.ua", True, True, "Accessible"),
        ("https://www.google.com.ua", False, True, "Not accessible"),
        ("https://www.google.com.ua", True, False, "Not accessible"),
        ("https://www.google.com.ua", False, False, "Not accessible")
    ],
    ids=[
        "if valid url and has internet connection,"
        " it should return 'Accessible'",
        "if the URL is invalid url and has internet connection,"
        " it should return 'Not accessible'",
        "if the URL valid but no internet connection,"
        " it should return 'Not accessible'",
        "if the URL is invalid and no internet connection,"
        " it should return 'Not accessible'"

    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
        mock_valid_google_url: Callable,
        mock_has_internet_connection: Callable,
        url: str,
        valid_url: bool,
        connection: bool,
        result: str
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = connection
    assert can_access_google_page(url) == result
