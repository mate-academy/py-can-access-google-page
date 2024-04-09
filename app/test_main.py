import pytest
from unittest import mock
from typing import Any

from app.main import can_access_google_page


@pytest.fixture
def mocked_validation() -> Any:
    with mock.patch("app.main.valid_google_url") as mocked_validation:
        yield mocked_validation


@pytest.fixture
def mocked_connection() -> Any:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


@pytest.mark.parametrize(
    "validation_return,connection_return,access_return",
    [
        pytest.param(True,
                     True,
                     "Accessible",
                     id="when validation and connection are true, "
                        "page should be accessible"),

        pytest.param(True,
                     False,
                     "Not accessible",
                     id="when validation is true and no connection, "
                        "page should not be accessible"),

        pytest.param(False,
                     True,
                     "Not accessible",
                     id="when no validation and connection is true, "
                        "page should not be accessible"),

        pytest.param(False,
                     False,
                     "Not accessible",
                     id="when no validation and no connection "
                        "are true, page should not be accessible")
    ]
)
def test_can_access_google_page(
        mocked_validation: Any,
        mocked_connection: Any,
        validation_return: bool,
        connection_return: bool,
        access_return: str
) -> None:
    can_access_google_page("")
    mocked_validation.assert_called_once()
    mocked_connection.assert_called_once()
    mocked_validation.return_value = validation_return
    mocked_connection.return_value = connection_return
    assert can_access_google_page("") == access_return
