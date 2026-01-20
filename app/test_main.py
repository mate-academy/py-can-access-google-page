from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,has_connection,status",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "should be accessible when both conditions are met",
        "shouldn't be accessible when only valid url are provided",
        "shouldn't be accessible when only connection are provided",
        "shouldn't be accessible when both conditions aren't met",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_connection: mock.MagicMock,
        mock_valid_url: mock.MagicMock,
        has_connection: bool,
        valid_url: bool,
        status: str
) -> None:
    mock_connection.return_value = has_connection
    mock_valid_url.return_value = valid_url
    assert can_access_google_page("url") == status
