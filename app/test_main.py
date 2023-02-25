import pytest
from unittest import mock
from app.main import can_access_google_page


class TestUrl:
    @pytest.mark.parametrize(
        "url, valid_url, has_internet, expected_result",
        [
            ("https://google.com",
             True,
             True,
             "Accessible"),
            ("https://google.com",
             False,
             False,
             "Not accessible"),
            ("https://google.com",
             True,
             False,
             "Not accessible"),
            ("https://google.com",
             False,
             True,
             "Not accessible")
        ])
    def test_can_access_google_page(
            self,
            url: str,
            valid_url: str,
            has_internet: bool,
            expected_result: bool
    ) -> None:
        with mock.patch(
                "app.main.valid_google_url", return_value=valid_url
        ), mock.patch(
            "app.main.has_internet_connection", return_value=has_internet
        ):
            assert can_access_google_page(url) == expected_result
