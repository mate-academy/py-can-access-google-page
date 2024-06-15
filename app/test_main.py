from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_net_connection, valid_url",
    [
        (True, True),
        (6, True),
        (14, True),
        (23, True),
        (6, 200)

    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet_connection: mock,
                                mock_valid_google_url: mock,
                                has_net_connection: bool | int,
                                valid_url: bool | int) -> None:
    mock_has_internet_connection.return_value = has_net_connection
    mock_valid_google_url.return_value = valid_url
    can_access_google_page("https://www.google.com")
    mock_has_internet_connection.assert_called_once()
    mock_valid_google_url.assert_called_once()
