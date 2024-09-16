from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_status,connection,message",
    [
        (1, 1, "Accessible"),
        (1, 0, "Not accessible"),
        (0, 1, "Not accessible")
    ]
)
def test_return_access(url_status, connection, message):
    with mock.patch("app.main.valid_google_url") as valid_url:
        valid_url.return_value = bool(url_status)
        with mock.patch("app.main.has_internet_connection") as connect:
            connect.return_value = bool(connection)
            response = can_access_google_page("https://ru.wikipedia.org")
            assert response == message
