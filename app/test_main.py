from unittest.mock import patch
from typing import Any

from pytest import mark
from pytest import fixture
from pytest import param


from app.main import can_access_google_page


@fixture()
def income_url() -> str:
    return "https://www.google.com/"


@mark.parametrize(
    "has_connection, valid_url, exp_result",
    [
        param(True, True, "Accessible",
              id="All correct"),
        param(False, False, "Not accessible",
              id="No connection and invalid url"),
        param(False, True, "Not accessible",
              id="No internet connection"),
        param(True, False, "Not accessible",
              id="Invalid url")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(mocked_valid_google_url: Any,
                                mocked_has_internet_connection: Any,
                                has_connection: bool,
                                valid_url: bool,
                                income_url: str,
                                exp_result: str
                                ) -> None:

    mocked_has_internet_connection.return_value = has_connection
    mocked_valid_google_url.return_value = valid_url
    assert can_access_google_page(income_url) == exp_result
