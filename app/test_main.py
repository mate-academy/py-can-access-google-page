from unittest import mock
from unittest.mock import Mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "first_res, second_res, fin_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_two_func_was_called(
        mocked_has_connection: Mock,
        mocked_valid_url: Mock,
        first_res: bool,
        second_res: bool,
        fin_result: str
) -> None:
    url = "http://google.com"
    mocked_has_connection.return_value = first_res
    mocked_valid_url.return_value = second_res
    assert can_access_google_page(url) == fin_result
