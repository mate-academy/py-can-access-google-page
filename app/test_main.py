from typing import Any, Generator

import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "validator_response, connection_response, access_response",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="should return Accessible if url \
            is valid and has internet connection",
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="should return 'Not Accessible' if url \
            is valid and no internet connection",
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="should return 'Not Accessible' if url \
            is not valid and has internet connection",
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="should return 'Not Accessible' if url \
            is not valid and no internet connection",
        ),
    ],
)
def test_access_with_mocked_page_validation_and_connection(
    validator_response: bool, connection_response: bool, access_response: str
) -> None:
    with mock.patch(
        "app.main.valid_google_url"
    ) as mocked_validator, mock.patch(
        "app.main.has_internet_connection"
    ) as mocked_connection:
        mocked_validator.return_value = validator_response
        mocked_connection.return_value = connection_response
        assert can_access_google_page("url_sample") == access_response


class TestFunctionsCall:
    @pytest.fixture(scope="class")
    def mocking_validator(
        self,
    ) -> Generator[mock.MagicMock | mock.AsyncMock, Any, None]:
        with mock.patch("app.main.valid_google_url") as mocked_validator:
            yield mocked_validator

    @pytest.fixture(scope="class")
    def mocking_connection(
        self,
    ) -> Generator[mock.MagicMock | mock.AsyncMock, Any, None]:
        with mock.patch(
            "app.main.has_internet_connection"
        ) as mocked_connection:
            yield mocked_connection

    def test_should_call_validator_function(
        self, mocking_validator: mock.MagicMock
    ) -> None:
        can_access_google_page("url_sample")
        mocking_validator.assert_called_once

    def test_should_call_connection_function(
        self, mocking_connection: mock.MagicMock
    ) -> None:
        can_access_google_page("url_sample")
        mocking_connection.assert_called_once

    def test_should_call_both_functions(
        self,
        mocking_validator: mock.MagicMock,
        mocking_connection: mock.MagicMock,
    ) -> None:
        can_access_google_page("url_sample")
        mocking_validator.assert_called
        mocking_connection.assert_called

    def test_should_transfer_url_to_page_validator(
        self, mocking_validator: mock.MagicMock
    ) -> None:
        can_access_google_page("url_sample")
        mocking_validator.assert_called_with("url_sample")
