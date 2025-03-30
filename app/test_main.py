from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, expected", [
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet_connection: mock.MagicMock,
                                mock_valid_google_url: mock.MagicMock,
                                valid_google_url: bool,
                                has_internet_connection: bool,
                                expected: str) -> None:
    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page("https://www.google.com/") == expected
