from unittest import mock
from typing import Callable

import pytest

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.mark.parametrize(
        "internet_response,valid_url_response,expected_response",
        [
            pytest.param(
                False, True, "Not accessible",
                id="should not access page if no internet"
            ),
            pytest.param(
                True, False, "Not accessible",
                id="should not access page if url invalid"
            ),
            pytest.param(
                False, False, "Not accessible",
                id="should not access page if no internet and url invalid"
            ),
            pytest.param(
                True, True, "Accessible",
                id="should access page if internet connection ok and url valid"
            ),
        ]
    )
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_correct_response(
            self,
            mocked_valid_url_check: Callable,
            mocked_internet_connection_check: Callable,
            internet_response: bool,
            valid_url_response: bool,
            expected_response: str
    ) -> None:
        mocked_internet_connection_check.return_value = internet_response
        mocked_valid_url_check.return_value = valid_url_response
        assert (can_access_google_page("https://some-page.com/")
                == expected_response)

    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_valid_url_call(
            self,
            mocked_valid_url_check: Callable,
            mocked_internet_connection_check: Callable
    ) -> None:
        url = "https://some-page.com/"
        can_access_google_page(url)
        mocked_valid_url_check.assert_called_once_with(url)

    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_internet_connection_call(
            self,
            mocked_valid_url_check: Callable,
            mocked_internet_connection_check: Callable
    ) -> None:
        url = "https://some-page.com/"
        can_access_google_page(url)
        mocked_internet_connection_check.assert_called_once()
