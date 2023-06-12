from app.main import can_access_google_page

from unittest.mock import patch


def test_can_access_google_page_correct_result() -> None:
    with (patch("app.main.valid_google_url") as response,
          patch("app.main.has_internet_connection") as current_time):
        response.return_value = True
        current_time.return_value = True
        assert can_access_google_page("") == "Accessible"

        response.return_value = False
        current_time.return_value = True
        assert can_access_google_page("") == "Not accessible"

        response.return_value = False
        current_time.return_value = False
        assert can_access_google_page("") == "Not accessible"

        response.return_value = True
        current_time.return_value = False
        assert can_access_google_page("") == "Not accessible"
