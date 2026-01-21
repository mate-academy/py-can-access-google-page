from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "google_url, internet_connection, message",
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
        mock_google_url: mock,
        mock_internet_connection: mock,
        google_url: bool,
        internet_connection: bool,
        message: str
) -> None:
    mock_internet_connection.return_value = internet_connection
    mock_google_url.return_value = google_url
    assert can_access_google_page("https://test_url") == message
