from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,has_connection,result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_access_with_different_parameters(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock,
        valid_url: bool,
        has_connection: bool,
        result: str
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_connection
    assert can_access_google_page("/") == result


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_func_was_called_once(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock
) -> None:
    can_access_google_page("/")
    mock_valid_google_url.assert_called_once_with("/")
    mock_has_internet_connection.assert_called_once()
