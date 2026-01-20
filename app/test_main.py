import pytest
from app.main import can_access_google_page
from unittest import mock


@pytest.mark.parametrize(
    "url, correct_url, connection, result",
    [
        ("https://www.amazon.com", False, True, "Not accessible"),
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_access_to_google_page(check_url: mock,
                               check_connection: mock,
                               url: str,
                               correct_url: bool,
                               connection: bool,
                               result: str) -> None:
    check_connection.return_value = connection
    check_url.return_value = correct_url
    assert (
        can_access_google_page(url) == result
    )
