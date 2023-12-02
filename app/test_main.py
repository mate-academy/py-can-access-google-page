import pytest
from unittest import mock
from typing import Callable
from app.main import can_access_google_page


class TestCanAccessGooglePage:
    tested_url = "https://www.google.com"

    @staticmethod
    @pytest.fixture
    def mocked_has_internet_connection() -> None:
        with (mock.patch("app.main.has_internet_connection")
              as mocked_internet_connection):
            yield mocked_internet_connection

    @staticmethod
    @pytest.fixture
    def mocked_valid_google_url() -> None:
        with mock.patch(
                "app.main.valid_google_url") as mocked_google_url:
            yield mocked_google_url

    def test_has_internet_connection_called(
            self,
            mocked_has_internet_connection: Callable
    ) -> None:
        can_access_google_page(self.tested_url)
        mocked_has_internet_connection.assert_called_once()

    def test_valid_google_url_called_with(
            self,
            mocked_valid_google_url: Callable
    ) -> None:
        can_access_google_page(self.tested_url)
        mocked_valid_google_url.assert_called_once_with(self.tested_url)

    @pytest.mark.parametrize(
        "valid_url,internet_connection,result",
        [
            pytest.param(True, True, "Accessible",
                         id="test accessible when all conditions are met"),
            pytest.param(False, True, "Not accessible",
                         id="test not accessible with url is not valid"),
            pytest.param(True, False, "Not accessible",
                         id="test not accessible with no connection")
        ]
    )
    def test_can_access(
            self,
            valid_url: bool,
            internet_connection: bool,
            result: str,
            mocked_valid_google_url: Callable,
            mocked_has_internet_connection: Callable
    ) -> None:
        mocked_valid_google_url.return_value = valid_url
        mocked_has_internet_connection.return_value = internet_connection
        assert can_access_google_page(self.tested_url) == result
