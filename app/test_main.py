import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize("internet_connection, google_url, expected_result", [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible")
])
def test_can_access_google_page(internet_connection: bool,
                                google_url: bool,
                                expected_result: str) -> None:
    with mock.patch("app.main.valid_google_url", return_value=google_url):
        with mock.patch("app.main.has_internet_connection",
                        return_value=internet_connection):
            result = can_access_google_page("https://www.google.com")
            assert result == expected_result
