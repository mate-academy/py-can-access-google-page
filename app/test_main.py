import datetime
import time
from typing import Any
import pytest
from unittest import TestCase, mock
from requests.exceptions import MissingSchema

from app.main import (can_access_google_page,
                      valid_google_url,
                      has_internet_connection)


class TestInternetConnectionClass(TestCase):
    def test_internet_connection_with_mock_time(self) -> None:
        with mock.patch("datetime.datetime") as mock_datetime:
            mock_datetime.now.return_value = datetime.datetime(
                2001, 2, 2, 10, 0, 0
            )
            result = has_internet_connection()
            self.assertFalse(result)
            mock_datetime.now.assert_called_once()


class TestValidUrlClass:
    @pytest.mark.parametrize(
        "url, expected_error",
        [
            pytest.param(1, MissingSchema, id="test_invalid_google_url"),
            pytest.param("", MissingSchema, id="test_invalid_google_url"),
            pytest.param(1123, MissingSchema, id="test_invalid_google_url"),
            pytest.param("htlsa", MissingSchema, id="test_invalid_google_url")
        ]
    )
    def test_invalid_google_url(self,
                                url: str,
                                expected_error: MissingSchema
                                ) -> None:
        with pytest.raises(expected_error):
            valid_google_url(url)


class TestCanAccessGooglePage(TestCase):
    @mock.patch("requests.get")
    @mock.patch("app.main.has_internet_connection")
    def test_all_functions_are_called(self,
                                      mock_has_internet: Any,
                                      mock_get: Any
                                      ) -> None:
        mock_has_internet.return_value = True
        mock_get.return_value.status_code = 200
        result = can_access_google_page("https://www.google.com/")

        mock_has_internet.assert_called_once()
        mock_get.assert_called_once_with("https://www.google.com/")
        self.assertEqual(result, "Accessible")

    def test_can_access_google_page_execution_time(self) -> None:
        start_time = time.time()

        result = can_access_google_page("https://www.google.com/")

        end_time = time.time()
        duration = end_time - start_time
        print(f"Function execution time: {duration: .4f} seconds")

        self.assertEqual(result, "Accessible")
