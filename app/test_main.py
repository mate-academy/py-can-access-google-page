import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url_result, internet_result, expected_message",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        valid_url_result: str,
        internet_result: str,
        expected_message: str
) -> None:
    with patch("app.main.valid_google_url") as mocked_url, \
         patch("app.main.has_internet_connection") as mocked_internet:
        mocked_url.return_value = valid_url_result
        mocked_internet.return_value = internet_result
        result = can_access_google_page("http://google.com")
        assert result == expected_message
