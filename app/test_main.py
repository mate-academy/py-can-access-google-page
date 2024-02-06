from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    ("valid_url", "has_connection", "expected_result"),
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
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock,
        valid_url: bool,
        has_connection: bool,
        expected_result: str
) -> None:
    mock_has_internet_connection.return_value = has_connection
    mock_valid_google_url.return_value = valid_url
    assert can_access_google_page("https://google.com/") == expected_result
