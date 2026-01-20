import pytest
from unittest import mock
from typing import Callable

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url_return_value,"
    "internet_connection_return_value,"
    "result",
    [
        pytest.param(
            True, False, "Not accessible",
            id="should return 'Not accessible' when no internet connection"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="should return 'Not accessible' when not valid url"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="should return 'Not accessible' when both False"
        ),
        pytest.param(
            True, True, "Accessible",
            id="should return 'Accessible' when both True"
        ),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_valid_google_url: Callable,
        mocked_internet_connection: Callable,
        valid_google_url_return_value: bool,
        internet_connection_return_value: bool,
        result: str
) -> None:
    mocked_valid_google_url.return_value = valid_google_url_return_value
    mocked_internet_connection.return_value = internet_connection_return_value
    assert can_access_google_page("asdf") == result
