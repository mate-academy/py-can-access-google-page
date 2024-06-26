import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize("has_internet, valid_url, expected",
                         [
                             (True, True, "Accessible"),
                             (False, True, "Not accessible"),
                             (True, False, "Not accessible"),
                             (False, False, "Not accessible")
                         ])
@patch("app.valid_google_url")
@patch("app.has_internet_connection")
def test_can_access_google_page(mock_has_internet_connection: bool,
                                mock_valid_google_url: bool,
                                has_internet: bool,
                                valid_url: bool,
                                expected: str) -> None:
    mock_has_internet_connection.return_value = has_internet
    mock_valid_google_url.return_value = valid_url

    url = "https://www.google.com"
    assert can_access_google_page(url) == expected
