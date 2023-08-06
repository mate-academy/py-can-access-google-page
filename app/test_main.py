import pytest
from unittest import mock
from app import main


@pytest.mark.parametrize("url, expected_result", [
    ("https://www.google.com", "Accessible"),
    ("https://www.this-url-does-not-exist.com", "Not accessible"),
    ("https://www.google.com/nonexistentpage", "Not accessible")
])
def test_can_access_google_page(url: str, expected_result: str) -> None:
    with mock.patch("app.main.has_internet_connection",
                    return_value=True if "nonexistentpage"
                                         not in url else False):
        with mock.patch("app.main.valid_google_url",
                        return_value=True if "google" in url else False):
            assert main.can_access_google_page(url) == expected_result
