from unittest.mock import patch
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, is_connected, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "accessible_when_both_true",
        "not_accessible_invalid_url",
        "not_accessible_no_internet",
        "not_accessible_both_false"
    ]
)
def test_can_access_google_page(
    is_valid_url: bool,
    is_connected: bool,
    expected: str
) -> None:
    with patch("app.main.valid_google_url") as mocked_url, \
         patch("app.main.has_internet_connection") as mocked_connection:

        mocked_url.return_value = is_valid_url
        mocked_connection.return_value = is_connected

        assert can_access_google_page("http://google.com") == expected
