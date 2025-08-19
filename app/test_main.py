from typing import Any, Generator

import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mocking_validator(
    request: pytest.FixtureRequest,
) -> Generator[mock.MagicMock | mock.AsyncMock, Any, None]:
    validator_return = getattr(request, "param", True)
    with mock.patch("app.main.valid_google_url") as mocked_validator:
        mocked_validator.return_value = validator_return
        yield mocked_validator


@pytest.fixture()
def mocking_connection(
    request: pytest.FixtureRequest,
) -> Generator[mock.MagicMock | mock.AsyncMock, Any, None]:
    connection_return = getattr(request, "param", True)
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        mocked_connection.return_value = connection_return
        yield mocked_connection


@pytest.mark.parametrize(
    "mocking_validator, mocking_connection, access_response",
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
    indirect=["mocking_validator", "mocking_connection"],
)
def test_access_with_mocked_page_validation_and_connection(
    mocking_validator: mock.MagicMock,
    mocking_connection: mock.MagicMock,
    access_response: str,
) -> None:
    assert can_access_google_page("url_sample") == access_response


class TestFunctionsCall:
    def test_should_call_validator_function(
        self, mocking_validator: mock.MagicMock
    ) -> None:
        can_access_google_page("url_sample")
        mocking_validator.assert_called_once()

    def test_should_call_connection_function(
        self,
        mocking_connection: mock.MagicMock,
        mocking_validator: mock.MagicMock
    ) -> None:
        can_access_google_page("url_sample")
        mocking_connection.assert_called_once()

    def test_should_call_both_functions_if_conditions_true(
        self,
        mocking_validator: mock.MagicMock,
        mocking_connection: mock.MagicMock,
    ) -> None:
        can_access_google_page("url_sample")
        mocking_validator.assert_called_once()
        mocking_connection.assert_called_once()

    @pytest.mark.parametrize(
        "mocking_connection, mocking_validator",
        [pytest.param(False, True)],
        indirect=["mocking_connection", "mocking_validator"],
    )
    def test_should_not_call_validator_function_if_connection_false(
        self,
        mocking_connection: mock.MagicMock,
        mocking_validator: mock.MagicMock,
    ) -> None:
        can_access_google_page("url_sample")
        mocking_connection.assert_called_once()
        mocking_validator.assert_not_called()

    def test_should_transfer_url_to_page_validator(
        self, mocking_validator: mock.MagicMock
    ) -> None:
        can_access_google_page("url_sample")
        mocking_validator.assert_called_once_with("url_sample")
