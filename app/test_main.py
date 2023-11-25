import pytest
from unittest import mock

from app.main import can_access_google_page

test_data = [
    ("www.google.com", True, True, "Accessible"),
    ("www.google.com", True, False, "Not accessible"),
    ("www.google.com", False, True, "Not accessible"),
    ("www.google.com", False, False, "Not accessible"),
]
test_ids = [
    "Should return \"Accessible\" if URL is valid and internet connection "
    "is present",
    "Should return \"Not accessible\" if URL is invalid",
    "Should return \"Not accessible\" if internet connection is absent",
    "Should return \"Not accessible\" if URL is invalid and internet "
    "connection is absent",
]


@pytest.mark.parametrize(
    "url, has_connection, url_valid, result",
    test_data,
    ids=test_ids
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_connection: mock,
        mock_valid_url: mock,
        url: str,
        has_connection: bool,
        url_valid: bool,
        result: str,
) -> None:
    mock_connection.return_value = has_connection
    mock_valid_url.return_value = url_valid
    assert can_access_google_page(url) == result
