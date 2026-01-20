import pytest
import requests

from unittest import mock
from typing import Type

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "url_test,"
        " valid_google_url_value,"
        " has_internet_connection_value,"
        " expected",
        [
            ("https://www.google.com", True, True, "Accessible"),
            ("https://www.google.co", False, True, "Not accessible"),
            ("https://www.google.com", True, False, "Not accessible"),
        ],
        ids=["accessible", "invalid_url", "no_internet"]
    )
    @mock.patch("app.main.valid_google_url")
    @mock.patch("app.main.has_internet_connection")
    def test_can_access_google_page(self,
                                    mocked_has_internet_connection: bool,
                                    mocked_valid_google_url: bool,
                                    url_test: str,
                                    valid_google_url_value: bool,
                                    has_internet_connection_value: bool,
                                    expected: str) -> None:
        mocked_valid_google_url.return_value = valid_google_url_value
        mocked_has_internet_connection.return_value =\
            has_internet_connection_value
        assert can_access_google_page(url_test) == expected


class TestExpectedError:
    @pytest.mark.parametrize(
        "url_test, expected_error",
        [
            pytest.param(
                5,
                requests.exceptions.MissingSchema,
                id="should raise MissingSchema if url is not a valid URL"
            ),
        ]
    )
    def test_raising_correctly(
            self,
            url_test: str,
            expected_error: Type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            can_access_google_page(url_test)
