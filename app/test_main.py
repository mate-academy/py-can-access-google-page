from collections.abc import Callable
from typing import Any
from unittest.mock import patch
import pytest
from app.main import can_access_google_page


@pytest.fixture()
def mocked_valid_google_url(request: Any) -> Any:
    value = request.param
    with patch("app.main.valid_google_url", return_value=value) as mock:
        yield mock


@pytest.fixture()
def mocked_has_internet_connection(request: Any) -> Any:
    value = request.param
    with patch("app.main.has_internet_connection", return_value=value) as mock:
        yield mock


@pytest.mark.parametrize(
    "mocked_valid_google_url, mocked_has_internet_connection, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Valid Google URL and has internet connection",
        "Valid Google URL and has no internet connection",
        "Invalid Google URL and has internet connection",
        "Invalid Google URL and has no internet connection",
    ],
    indirect=["mocked_valid_google_url", "mocked_has_internet_connection"]
)
def test_can_access_google_page(
        mocked_valid_google_url: Callable,
        mocked_has_internet_connection: Callable,
        result: str
) -> None:
    assert can_access_google_page("https://google.com") == result
