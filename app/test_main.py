import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_connection,is_valid_url,is_access",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mocked_connection: mock,
    mocked_url: mock,
    is_connection: bool,
    is_valid_url: bool,
    is_access: str
) -> None:
    mocked_connection.return_value = is_connection
    mocked_url.return_value = is_valid_url
    assert can_access_google_page("https://www.google.com.ua/") == is_access
