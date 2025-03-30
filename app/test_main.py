import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,"
    "check_valid,"
    "check_internet,"
    "expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", False, True, "Not accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.google.com", False, False, "Not accessible")
    ])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_valid_google_url: bool,
                                mock_has_internet_connection: bool,
                                url: str,
                                check_valid: bool,
                                check_internet: bool,
                                expected_result: str) -> None:
    mock_valid_google_url.return_value = check_valid
    mock_has_internet_connection.return_value = check_internet
    assert can_access_google_page("https://www.google.com") == expected_result
