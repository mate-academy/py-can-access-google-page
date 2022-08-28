from unittest import mock
import pytest
from app.main import can_access_google_page


class Test:
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    @pytest.mark.parametrize(
        "url, expected_result",
        [
            ("google.com", "Not accessible"),
            ("facebook.com", "Not accessible"),
        ]
    )
    def test_cant_access_google(self, mock1, mock2, url, expected_result):
        mock1.return_value = False
        mock2.return_value = True
        assert can_access_google_page(url) == expected_result


class Test2:
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    @pytest.mark.parametrize(
        "url, expected_result",
        [
            ("google.com", "Not accessible"),
            ("facebook.com", "Not accessible"),
        ]
    )
    def test_cant_access_one_false(self, mock1, mock2, url, expected_result):
        mock1.return_value = True
        mock2.return_value = False
        assert can_access_google_page(url) == expected_result
