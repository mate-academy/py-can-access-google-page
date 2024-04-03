import pytest
from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url_return, has_internet_connection_return, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock,
        has_internet_connection_return: bool,
        valid_google_url_return: bool,
        expected_result: str
) -> None:
    mock_has_internet_connection.return_value = has_internet_connection_return
    mock_valid_google_url.return_value = valid_google_url_return

    assert can_access_google_page("url") == expected_result

    mock_has_internet_connection.assert_called_once()
    if has_internet_connection_return:
        mock_valid_google_url.assert_called_once()
    else:
        mock_valid_google_url.assert_not_called()
