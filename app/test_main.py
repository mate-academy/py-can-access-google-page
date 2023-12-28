from unittest import mock

import app
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    app.main.has_internet_connection = mock.MagicMock()
    app.main.valid_google_url = mock.MagicMock()
    assert can_access_google_page("http://google.com") == "Accessible"
