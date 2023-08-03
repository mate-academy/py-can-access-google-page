from unittest import mock
import pytest
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
@pytest.mark.parametrize(
    "valid_google_url", "has_internet_connection", "expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock,
        has_internet_connection: bool,
        valid_google_url: str,
        expected_result: str
) -> None:
    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet_connection.return_value = has_internet_connection

    result = can_access_google_page("https://maps.google.com/")
    assert result == expected_result
