import pytest
from app.main import can_access_google_page
from unittest import mock


@pytest.mark.parametrize(
    "url,connection, result",
    [
        ("https://www.amazon.com", True, "Not accessible"),
        ("https://www.google.com", True, "Accessible"),
        ("https://www.google.com", False, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
def test_access_to_google_page(check_connection, url, connection, result) -> None:
    check_connection.return_value = connection
    assert (
        can_access_google_page(url) == result
    )
