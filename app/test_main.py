from unittest import mock
import pytest

from app.main import can_access_google_page


class TestUrl:

    @pytest.mark.parametrize(
        "valid_url, has_internet, expected_result",
        [
            (True,
             True,
             "Accessible"),
            (False,
             False,
             "Not accessible"),
            (True,
             False,
             "Not accessible"),
            (False,
             True,
             "Not accessible")
        ])
    def test_can_access_google_page(
            self,
            valid_url: str,
            has_internet: bool,
            expected_result: bool
    ) -> None:
        url = "https://google.com"
        with mock.patch(
                "app.main.valid_google_url", return_value=valid_url
        ), mock.patch(
            "app.main.has_internet_connection", return_value=has_internet
        ):
            assert can_access_google_page(url) == expected_result
