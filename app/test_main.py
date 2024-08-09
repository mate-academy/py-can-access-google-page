from unittest import mock
from app.main import can_access_google_page
import pytest

URL = "http://www.google.com"


@pytest.fixture()
def mocked_current_time() -> None:
    with mock.patch("app.main.datetime") as mock_current_time:
        yield mock_current_time


@pytest.fixture()
def first_func() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_valid_google_url:
        yield mocked_valid_google_url


@pytest.fixture()
def sec_func() -> None:
    with (mock.patch("app.main.has_internet_connection")
          as mocked_has_internet_connection):
        yield mocked_has_internet_connection


@pytest.mark.parametrize(
    "url, value_first_func, value_sec_func, result",
    [
        pytest.param(
            URL,
            True,
            True,
            "Accessible",
            id="should return accessible when funcs true"
        ),
        pytest.param(
            URL,
            False,
            True,
            "Not accessible",
            id="should return not accessible when first func false"
        ),
        pytest.param(
            URL,
            True,
            False,
            "Not accessible",
            id="should return not accessible when second func false"
        ),
        pytest.param(
            URL,
            False,
            False,
            "Not accessible",
            id="should return not accessible when all funcs false"
        ),
    ]
)
def test_should_return_accessible_when_all_funcs_return_true(
        first_func: mock,
        sec_func: mock,
        url: str,
        value_first_func: bool,
        value_sec_func: bool,
        result: str
) -> None:
    first_func.return_value = value_first_func
    sec_func.return_value = value_sec_func
    assert can_access_google_page(url) == result, (
        f"{result} when valid_google_url returned "
        f"{value_first_func} and has_internet_connection returned "
        f"{value_sec_func} but got {can_access_google_page(url)} instead"
    )
