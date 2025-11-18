from unittest.mock import patch
from app.main import can_access_google_page


def test_if_can_it_connect_to_internet_and_first_condition():
    with patch("app.main.valid_google_url")