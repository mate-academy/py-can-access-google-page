from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "func_1_result,func_2_result,total_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible")
    ]
)
def test_test_main_when_internet_connection_and_valid_url(
        func_1_result: bool,
        func_2_result: bool,
        total_result: str
) -> None:
    with (mock.patch("app.main.has_internet_connection") as ic,
          mock.patch("app.main.valid_google_url") as url):
        ic.return_value = func_1_result
        url.return_value = func_2_result
        assert can_access_google_page("http://www.google.com") == total_result
