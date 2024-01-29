from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, google_url, result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
    ],
    ids=[
        "Should return 'Accessible' if has connection and correct url",
        "Should return 'Not accessible' if has not connection and correct url",
        "Should return 'Not accessible' if has not correct url",
        "Should return 'Not accessible' if has not correct connection",
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_google_page_accessibility(
        mock_internet_connection: mock.MagicMock,
        mock_valid_google_url: mock.MagicMock,
        internet_connection: bool,
        google_url: bool,
        result: str,
) -> None:
    mock_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = google_url
    assert can_access_google_page("https://www.google.com/") == result
