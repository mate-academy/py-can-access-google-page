import pytest
from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "google_url,has_internet,is_access",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(mocked_valid_google_url: mock,
                                mocked_has_internet_connection: mock,
                                google_url: bool,
                                has_internet: bool,
                                is_access: str) -> None:
    mocked_valid_google_url.return_value = google_url
    mocked_has_internet_connection.return_value = has_internet
    result = can_access_google_page("https://www.google.com.ua")
    assert result == is_access
