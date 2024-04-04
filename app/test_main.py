from typing import Callable
from unittest.mock import patch

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_url,is_internet,expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "return 'Accessible' if url is valid and there is internet access",
        "return 'Not accessible' if url is not valid",
        "return 'Not accessible' if there is no internet",
        "return 'Not accessible' if url is not valid and there is no internet",
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mocked_internet_func: Callable,
    mocked_url_func: Callable,
    is_internet: bool,
    is_url: bool,
    expected: str
) -> None:
    mocked_internet_func.return_value = is_internet
    mocked_url_func.return_value = is_url
    assert can_access_google_page("url") == expected
