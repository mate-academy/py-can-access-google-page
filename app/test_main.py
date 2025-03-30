import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "correct_url, connection_status, access_status",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_valid_google_url: mock.MagicMock,
                                mock_has_internet_connection: mock.MagicMock,
                                correct_url: bool,
                                connection_status: bool,
                                access_status: str) -> None:

    mock_valid_google_url.return_value = correct_url
    mock_has_internet_connection.return_value = connection_status

    assert can_access_google_page("https://www.google.com") == access_status
