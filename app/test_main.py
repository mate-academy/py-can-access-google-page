import pytest
from unittest.mock import patch

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "has_internet, is_valid_url, expected",
        [
            pytest.param(True, True, "Accessible", id="internet_and_valid_url"),
            pytest.param(True, False, "Not accessible", id="internet_but_invalid_url"),
            pytest.param(False, True, "Not accessible", id="no_internet_but_valid_url"),
            pytest.param(False, False, "Not accessible", id="no_internet_and_invalid_url"),
        ],
    )
    def test_can_access_google_page(
        self, has_internet, is_valid_url, expected
    ):
        with patch("app.main.has_internet_connection", return_value=has_internet), \
             patch("app.main.valid_google_url", return_value=is_valid_url):
            assert can_access_google_page("https://google.com") == expected
