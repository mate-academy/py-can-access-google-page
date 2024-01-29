import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, connection, expected_message",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google(
        mock_valid_url: mock.MagicMock,
        mock_connection: mock.MagicMock,
        valid_url: bool,
        connection: bool,
        expected_message: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_connection.return_value = connection
    assert (can_access_google_page("https://www.google.com/")
            == expected_message)
