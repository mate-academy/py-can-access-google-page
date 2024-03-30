import pytest

from datetime import datetime
from unittest import mock
from typing import Callable

from app.main import (
    can_access_google_page,
    valid_google_url,
    has_internet_connection
)


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
class TestCanAccessGooglePage:

    @pytest.mark.parametrize(
        "has_connection_output, valid_url_output, result",
        [
            pytest.param(True, True, "Accessible"),
            pytest.param(False, True, "Not accessible"),
            pytest.param(True, False, "Not accessible"),
            pytest.param(False, False, "Not accessible"),
        ],
    )
    def test_should_return_correct_result(
        self,
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable,
        has_connection_output: bool,
        valid_url_output: bool,
        result: str,
    ) -> None:
        mocked_valid_google_url.return_value = has_connection_output
        mocked_has_internet_connection.return_value = valid_url_output
        assert can_access_google_page("test") == result

    def test_should_call_valid_google_url_func(
        self,
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable
    ) -> None:
        can_access_google_page("test")
        mocked_valid_google_url.assert_called_once_with("test")

    def test_should_call_has_internet_connection_func(
        self,
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable,
    ) -> None:
        can_access_google_page("test")
        mocked_has_internet_connection.assert_called_once()


@mock.patch("requests.get")
class TestValidUrl:

    @pytest.mark.parametrize(
        "status_code, output",
        [
            pytest.param(200, True),
            pytest.param(100, False),
            pytest.param(300, False),
            pytest.param(400, False),
            pytest.param(500, False),
            pytest.param(600, False),
        ],
    )
    def test_correct_result_depending_on_status_code(
        self,
        mocked_requests: Callable,
        status_code: int,
        output: bool
    ) -> None:
        mocked_requests.return_value.status_code = status_code
        assert valid_google_url("test") == output

    def test_should_call_requests_get_function(
        self,
        mocked_requests: Callable
    ) -> None:
        valid_google_url("test")
        mocked_requests.assert_called_once_with("test")


@mock.patch("datetime.datetime")
class TestHasInternetConnection:

    @pytest.mark.parametrize(
        "current_time, result",
        [
            pytest.param(datetime(2024, 3, 30, 6), True),
            pytest.param(datetime(2024, 3, 30, 12), True),
            pytest.param(datetime(2024, 3, 30, 22), True),
            pytest.param(datetime(2024, 3, 30, 23), False),
            pytest.param(datetime(2024, 3, 30, 0), False),
            pytest.param(datetime(2024, 3, 30, 4), False),
        ],
    )
    def test_should_return_correct_result_depends_on_time(
        self,
        mocked_datetime: Callable,
        current_time: Callable,
        result: bool
    ) -> None:
        mocked_datetime.now.return_value = current_time
        assert has_internet_connection() == result

    def test_should_call_datetime_now(
        self,
        mocked_datetime: Callable
    ) -> None:
        has_internet_connection()
        mocked_datetime.now.assert_called_once()
