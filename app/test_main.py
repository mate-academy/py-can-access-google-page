from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_net_connection, valid_url, is_connect",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet_connection: mock,
                                mock_valid_google_url: mock,
                                has_net_connection: bool | int,
                                valid_url: bool | int,
                                is_connect: str) -> None:
    mock_has_internet_connection.return_value = has_net_connection
    mock_valid_google_url.return_value = valid_url
    assert (can_access_google_page("https://www.google.com") == is_connect)
