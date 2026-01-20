from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page

import pytest


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "input_url,url_is_valid,has_internet,expected_result",
        [
            (
                "https://anyurl.com/",
                True,
                True,
                "Accessible"
            ),
            (
                "https://anyurl.com/",
                False,
                True,
                "Not accessible"
            ),
            (
                "https://anyurl.com/",
                True,
                False,
                "Not accessible"
            ),
            (
                "https://anyurl.com/",
                False,
                False,
                "Not accessible"
            )
        ],
        ids=[
            "Accessible when url is valid \
and Internet connection exists",
            "Not accessible when url is invalid \
and Internet connection exists",
            "Not accessible when url is valid \
and Internet connection does not exist",
            "Test when url is not valid and \
Internet connection does not exist"
        ]
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_paged(self,
                                     mocked_valid_google_url: MagicMock,
                                     mocked_has_internet: MagicMock,
                                     input_url: str,
                                     url_is_valid: bool,
                                     has_internet: bool,
                                     expected_result: str) -> None:
        mocked_valid_google_url.return_value = url_is_valid
        mocked_has_internet.return_value = has_internet
        assert can_access_google_page(input_url) == expected_result
