import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url_mock, connection_mock, expected_result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.google.com", False, True, "Not accessible"),
        ("некоректний_урл", False, False, "Not accessible"),
    ],
)
def test_can_access_google_page_різні_умови(
    url, valid_url_mock, connection_mock, expected_result
):
    with patch("app.main.valid_google_url", return_value=valid_url_mock), patch(
        "app.main.has_internet_connection", return_value=connection_mock
    ):
        assert can_access_google_page(url) == expected_result
