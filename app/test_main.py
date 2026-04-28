from typing import Any
from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize("url, connect, result",
                         [
                             (True, True, "Accessible"),
                             (True, False, "Not accessible"),
                             (False, True, "Not accessible"),
                             (False, False, "Not accessible"),
                         ])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_connection: Any,
        mock_valid: Any,
        url: bool,
        connect: bool,
        result: str
) -> None:
    mock_valid.return_value = url
    mock_connection.return_value = connect

    assert can_access_google_page("https://google.com") == result


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cannot_access_if_only_connection(
        mock_connection: Any,
        mock_valid: Any) -> None:
    mock_valid.return_value = False
    mock_connection.return_value = True

    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_cannot_access_if_only_valid_url(
        mock_connection: Any,
        mock_valid: Any) -> None:
    mock_valid.return_value = True
    mock_connection.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"
