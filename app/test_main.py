from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page():
    has_internet_connection = mock.MagicMock()
    valid_google_url = mock.MagicMock()
    assert can_access_google_page('http://google.com') == "Accessible"
