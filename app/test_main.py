from unittest.mock import MagicMock

import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize("valid_url, has_internet, result", [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible"),
])
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_google_url : MagicMock,
                                mock_has_internet_connection : MagicMock,
                                valid_url : bool,
                                has_internet : bool,
                                result: str) -> None:

    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_internet

    url = "https://google.com"
    assert can_access_google_page(url) == result

    mock_valid_google_url.assert_called_once_with(url)
    mock_has_internet_connection.assert_called_once()
