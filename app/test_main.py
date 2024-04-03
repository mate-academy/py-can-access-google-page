import pytest
from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "has_internet_connection_return, valid_google_url_return, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock,
        has_internet_connection_return: bool,
        valid_google_url_return: bool,
        expected_result: str
) -> None:
    mock_valid_google_url.return_value = valid_google_url_return
    mock_has_internet_connection.return_value = has_internet_connection_return

    can_access_google_page(".ya.ustal.delat`.etu.tasku.")

    mock_has_internet_connection.assert_called_once()
    if mock_has_internet_connection.return_value:
        mock_valid_google_url.assert_called_once()

    assert can_access_google_page("o4en`.ustal.") == expected_result
