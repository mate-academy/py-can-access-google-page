import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize("valid_google, has_internet, result", [
    (True, True, "Accessible"),
    (False, True, "Not accessible"),
    (True, False, "Not accessible"),
    (False, False, "Not accessible"),
])
def test_valid_url_and_connection_exists(
    valid_google: bool,
    has_internet: bool,
    result: str
) -> None:
    with (mock.patch("app.main.valid_google_url") as mock_valid_google_url,
         mock.patch("app.main.has_internet_connection") as
         mock_has_internet_connection):

        mock_valid_google_url.return_value = valid_google
        mock_has_internet_connection.return_value = has_internet

        url = "https://www.google.com"
        assert can_access_google_page(url) == result
        if has_internet:
            mock_valid_google_url.assert_called_once_with(url)
        mock_has_internet_connection.assert_called_once()
