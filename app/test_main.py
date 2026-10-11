from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_valid, internet, expected",
    [
        (True,
         True,
         "Accessible"),
        (True,
         False,
         "Not accessible"),
        (False,
         True,
         "Not accessible"),
        (False,
         False,
         "Not accessible")
    ],
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_google_url: bool,
                                mock_has_internet_connection: bool,
                                url_valid: bool,
                                internet: bool,
                                expected: str) -> None:
    mock_valid_google_url.return_value = url_valid
    mock_has_internet_connection.return_value = internet
    assert can_access_google_page("") == expected
