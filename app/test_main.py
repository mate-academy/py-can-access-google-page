import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize("internet_value, google_value, expected_result", [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible"),
])
def test_valid_internet_connection(
        internet_value: bool,
        google_value: bool,
        expected_result: str) -> None:

    with mock.patch("app.main.has_internet_connection") as mock_internet:
        with mock.patch("app.main.valid_google_url") as mock_google:
            mock_internet.return_value = internet_value
            mock_google.return_value = google_value
            result = can_access_google_page("https://google.com")
            assert result == expected_result
