from unittest import mock
from app.main import can_access_google_page


import pytest


@pytest.mark.parametrize("valid_situation, connection, result", [
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
def test_connection(mock_has_internet_connection: mock,
                    mock_valid_google_url: mock,
                    valid_situation: bool,
                    connection: bool,
                    result: str) -> None:
    mock_valid_google_url.return_value = valid_situation
    mock_has_internet_connection.return_value = connection

    assert can_access_google_page("https://itc.ua/") == result

    mock_has_internet_connection.assert_called_once()
    if connection:
        mock_valid_google_url.assert_called_once_with("https://itc.ua/")
    else:
        mock_valid_google_url.assert_not_called()
