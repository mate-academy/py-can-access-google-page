import pytest

from typing import Callable
from unittest import mock

from app.main import can_access_google_page


class TestCorrectResults:
    @pytest.mark.parametrize(
        "correct_url,"
        "valid_url_value,"
        "internet_connection_value,"
        "expected_access_value",
        [
            pytest.param(
                "https://www.google.com",
                True,
                True,
                "Accessible",
                id="connect time and ulr must be correct"
            ),
            pytest.param(
                "https://www.google.com",
                True,
                False,
                "Not accessible",
                id="connect time must be incorrect"
            ),
            pytest.param(
                "https://www.google.com",
                False,
                True,
                "Not accessible",
                id="url response must be incorrect"
            ),
            pytest.param(
                "https://www.google.com",
                False,
                False,
                "Not accessible",
                id="url response and connect time must be incorrect"
            ),
        ]
    )
    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_expected_correct_results(
            self,
            mock_internet_connection: Callable,
            mock_valid_google_url: Callable,
            correct_url: str,
            valid_url_value: bool,
            internet_connection_value: bool,
            expected_access_value: str,
    ) -> None:
        mock_valid_google_url.return_value = valid_url_value
        mock_internet_connection.return_value = internet_connection_value
        assert can_access_google_page(correct_url) == expected_access_value

    @mock.patch("app.main.has_internet_connection")
    @mock.patch("app.main.valid_google_url")
    def test_called_all_functions(
            self,
            mock_internet_connection: Callable,
            mock_valid_google_url: Callable,
    ) -> None:
        can_access_google_page("https://www.google.com")
        mock_internet_connection.assert_called_once()
        mock_valid_google_url.assert_called_once()
