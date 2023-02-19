import pytest
from unittest.mock import patch
from app.main import can_access_google_page
from typing import Callable


@pytest.fixture(params=[
    (True, True, "Accessible"),
    (False, True, "Not accessible"),
    (True, False, "Not accessible"),
    (False, False, "Not accessible")
])
def access_fixture(request: tuple) -> tuple:
    valid_mock, internet_mock, expected_result = request.param
    with (
        patch("app.main.valid_google_url", return_value=valid_mock),
        patch("app.main.has_internet_connection", return_value=internet_mock)
    ):
        yield valid_mock, internet_mock, expected_result


def test_can_access_google_page(access_fixture: Callable) -> None:
    valid_mock, internet_mock, expected_result = access_fixture
    url = "http://www.google.com"
    result = can_access_google_page(url)
    assert result == expected_result
