import pytest

from unittest.mock import patch
from typing import Callable

from app.main import can_access_google_page


@patch("requests.get")
@patch("datetime.datetime")
@pytest.mark.parametrize(
    "status_code,hour,can_access",
    [
        (200, 9, "Accessible"),
        (404, 22, "Not accessible"),
        (200, 5, "Not accessible"),
        (404, 2, "Not accessible")
    ],
    ids=[
        "Function must return `Accessible` when url is valid and time 6...23",
        "Function must return `Not accessible` when url is not valid",
        "Function must return `Not accessible` when time is not 6...23",
        ("Function must return `Not accessible` when url is not valid"
         "and time is not 6...23")
    ]
)
def test_can_access_google_page(
        mock_current_time: Callable,
        mock_request: Callable,
        status_code: int,
        hour: int,
        can_access: str
) -> None:

    mock_request.return_value.status_code = status_code
    mock_current_time.now.return_value.hour = hour

    assert can_access_google_page("") == can_access
