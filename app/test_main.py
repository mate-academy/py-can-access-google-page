import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_internet, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_valid_url_and_connection_exists(
        valid_url: bool,
        has_internet: bool,
        expected_result: str
) -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        with mock.patch("app.main.has_internet_connection") as mock_internet:
            mock_valid_url.return_value = valid_url
            mock_internet.return_value = has_internet

            result = can_access_google_page("https://www.google.com")
            assert result == expected_result
