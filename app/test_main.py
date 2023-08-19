import pytest

from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "internet_connection, google_url, expected_access",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access(
        mock_has_internet_connection: mock.MagicMock,
        mock_valid_google_url: mock.MagicMock,
        internet_connection: bool,
        google_url: bool,
        expected_access: str
) -> None:
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = google_url

    assert can_access_google_page("www.google.com") == expected_access
