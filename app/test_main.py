import pytest

from app.main import can_access_google_page
from unittest import mock


class TestFunc:
    @pytest.mark.parametrize(
        "response, current_time, result",
        [
            (True, True, "Accessible"),
            (True, False, "Not accessible"),
            (False, True, "Not accessible"),
            (False, False, "Not accessible"),
        ]
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(self,
                                    mock_google_url,
                                    mock_internet_connection,
                                    response,
                                    current_time,
                                    result
                                    ):
        mock_google_url.return_value = response
        mock_internet_connection.return_value = current_time
        assert can_access_google_page("google.com") == result


# class TestFunc:
#     @mock.patch("app.main.valid_google_url")
#     @mock.patch("app.main.has_internet_connection")
#     def test_can_access_google_page_1(self,
#                                       mock_google_url,
#                                       mock_internet_connection):
#         mock_internet_connection.return_value = datetime.time(6, 0, 0)
#         mock_google_url.return_value = True
#         assert can_access_google_page("google.com") == "Accessible"
#
#     @mock.patch("app.main.valid_google_url")
#     @mock.patch("app.main.has_internet_connection")
#     def test_can_access_google_page_2(self,
#                                       mock_google_url,
#                                       mock_internet_connection):
#         mock_internet_connection.return_value = datetime.time(10, 0, 0)
#         mock_google_url.return_value = False
#         assert can_access_google_page("google.com") == "Not accessible"
#
#     @mock.patch("app.main.valid_google_url")
#     @mock.patch("app.main.has_internet_connection")
#     def test_can_access_google_page_3(self,
#                                       mock_google_url,
#                                       mock_internet_connection):
#         mock_internet_connection.return_value = False
#         mock_google_url.return_value = True
#         assert can_access_google_page("google.com") == "Not accessible"
