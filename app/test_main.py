# write your code here
from app.main import can_access_google_page
from unittest import mock


def test_can_access_google_page():
    with (
        mock.patch("current_time") as mocked_current_time,
        mock.patch("response") as mocked_response
    ):
        mocked_current_time.return_value = True
        mocked_response.status_code.return_value = 200

        assert can_access_google_page() == "Accessible"