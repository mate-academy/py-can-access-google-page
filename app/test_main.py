from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


import pytest


@pytest.fixture
def test_url() -> str:
    return "https://itc.ua/"


@pytest.mark.parametrize("valid_url, exisiting_connection, result", [
    (False, False, "Not accessible"),
    (True, True, "Accessible"),
    (False, True, "Not accessible"),
    (True, False, "Not accessible"),
], ids=["No valid and no connected",
        "Valid and connected",
        "No valid but connected",
        "Valid but not connected"])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_connection(mock_has_internet_connection: MagicMock,
                    mock_valid_google_url: MagicMock,
                    valid_url: bool,
                    exisiting_connection: bool,
                    result: str) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = exisiting_connection

    assert can_access_google_page(test_url) == result

    mock_has_internet_connection.assert_called_once()
    if exisiting_connection:
        mock_valid_google_url.assert_called_once_with(test_url)
    else:
        mock_valid_google_url.assert_not_called()
