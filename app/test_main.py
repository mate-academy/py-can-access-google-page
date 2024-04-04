import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,internet_connection,expected_result",
    [
        ("https://www.google.com", True, "Accessible"),
        ("https://non-existent_google.com", True, "Not accessible"),
        ("https://www.google.com", False, "Not accessible")
    ],
    ids=["Existing URL and internet connection",
         "Non-existent URL is internet connection",
         "Existing URL  no internet connection"]
)
def test_can_access_google_page(valid_url: str,
                                internet_connection: bool,
                                expected_result: str) -> None:
    with patch("app.main.has_internet_connection",
               return_value=internet_connection):
        with patch("app.main.valid_google_url",
                   return_value=(valid_url == "https://www.google.com")):
            assert can_access_google_page(valid_url) == expected_result
