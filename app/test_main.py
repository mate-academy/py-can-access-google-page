from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize("url, internet, status", [
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (True, True, "Accessible"),
])
def test_can_access(url: bool, internet: bool, status: str) -> None:
    with mock.patch("app.main.valid_google_url",
                    return_value=url):
        with mock.patch("app.main.has_internet_connection",
                        return_value=internet):
            assert can_access_google_page("https://www.google.com") == status

# def test_with_url():
#     with mock.patch("app.main.valid_google_url", return_value=True),\
#         mock.patch("app.main.has_internet_connection", return_value=False):
#         assert can_access_google_page("https://www.google.com")
#         == "Not accessible"
#
# def test_with_all():
#     with patch("app.main.valid_google_url", return_value=True),\
#         patch("app.main.has_internet_connection", return_value=True):
#             assert can_access_google_page("https://www.google.com")
#             == "Accessible"
