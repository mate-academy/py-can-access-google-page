from unittest import mock

import app
from app.main import (can_access_google_page)


def test_can_access_google_page() -> None:
    url = "http://google.com"
    app.main.has_internet_connection = mock.MagicMock()
    app.main.valid_google_url = mock.MagicMock()
    can_access_google_page(url)
    app.main.has_internet_connection.assert_called_once()
    app.main.valid_google_url.assert_called_once_with(url)
