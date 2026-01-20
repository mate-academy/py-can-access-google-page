from unittest import mock
from app.main import can_access_google_page
from typing import Callable
import pytest


@pytest.mark.parametrize(
    "values,result", [
        pytest.param([True, True], "Accessible",
                     id="User don't have access with internet and valid url"),
        pytest.param([True, False], "Not accessible",
                     id="User has access without valid url"),
        pytest.param([False, True], "Not accessible",
                     id="User has access without internet"),
        pytest.param([False, False], "Not accessible",
                     id="User has access without internet and valid url"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_internet_con: Callable,
        mocked_google_url: Callable,
        values: list,
        result: str,
) -> None:
    mocked_internet_con.return_value, mocked_google_url.return_value = values
    assert can_access_google_page("google.com") == result
