import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url_mock, internet_mock, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    valid_url_mock: bool,
    internet_mock: bool,
    expected_result: str
) -> None:
    with patch("app.main.valid_google_url", return_value=valid_url_mock), \
         patch("app.main.has_internet_connection", return_value=internet_mock):
        assert can_access_google_page("https://example.com") == expected_result
