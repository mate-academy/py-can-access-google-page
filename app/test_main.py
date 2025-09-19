from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize("valid_url_return, internet_return, expected", [
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible"),
    (True, True, "Accessible"),
])
def test_valid_url_and_connection_exists_returns(valid_url_return: str,
                                                 internet_return: bool,
                                                 expected: bool) -> None:
    with (mock.patch("app.main.valid_google_url")
          as mock_valid_google_url,
          mock.patch("app.main.has_internet_connection")
          as mock_has_internet_connection):
        mock_valid_google_url.return_value = valid_url_return
        mock_has_internet_connection.return_value = internet_return

        result = can_access_google_page("url")

        assert result == expected
        mock_valid_google_url.assert_called_once_with("url")
        mock_has_internet_connection.assert_called_once()
