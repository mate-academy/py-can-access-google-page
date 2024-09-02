import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet_connection, valid_url, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.google.com", False, True, "Not accessible"),
        ("https://www.google.com", False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        url: str,
        internet_connection: bool,
        valid_url: bool,
        expected: str
) -> None:
    with patch(
            "app.main.has_internet_connection",
            return_value=internet_connection
    ):
        with patch(
                "app.main.valid_google_url", return_value=valid_url
        ):
            assert can_access_google_page(url) == expected
