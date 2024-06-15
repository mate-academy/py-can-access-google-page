from typing import Type
from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_net_connection, valid_url, error",
    [
        (True, True, None),
        (True, False, AssertionError),
        (False, True, AssertionError),
        (False, False, AssertionError),

    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet_connection: mock,
                                mock_valid_google_url: mock,
                                has_net_connection: bool | int,
                                valid_url: bool | int,
                                error: Type[Exception]) -> None:
    mock_has_internet_connection.return_value = has_net_connection
    mock_valid_google_url.return_value = valid_url
    try:
        can_access_google_page("https://www.google.com")
        mock_has_internet_connection.assert_called_once()
        mock_valid_google_url.assert_called_once()
    except Exception:
        with pytest.raises(error):
            can_access_google_page("https://www.google.com")
            mock_has_internet_connection.assert_called_once()
            mock_valid_google_url.assert_called_once()
