from typing import Any
import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.fixture
def mocked_google_page_environment(request: Any) -> bool:
    valid_google_url, internet_connection = request.param
    with patch(
        "app.main.valid_google_url", return_value=valid_google_url
    ), patch(
        "app.main.has_internet_connection", return_value=internet_connection
    ):
        yield


@pytest.mark.parametrize(
    "mocked_google_page_environment, expected_result",
    [
        ((True, True), "Accessible"),
        ((False, False), "Not accessible"),
        ((False, True), "Not accessible"),
        ((True, False), "Not accessible"),
    ],
    indirect=["mocked_google_page_environment"],
)
def test_accessible_google_page(
    mocked_google_page_environment: bool, expected_result: str
) -> None:
    assert can_access_google_page("www.google.com") == expected_result
