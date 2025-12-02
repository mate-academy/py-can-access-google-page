from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_internet_valid, mock_url_valid, return_value",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(mock_internet_valid: bool,
                                mock_url_valid: bool,
                                return_value: str) -> None:
    with mock.patch("app.main.valid_google_url") as mock_url,\
         mock.patch("app.main.has_internet_connection") as mock_internet:

        mock_url.return_value = mock_url_valid
        mock_internet.return_value = mock_internet_valid

        result = can_access_google_page("https://www.google.com")
        assert result == return_value
