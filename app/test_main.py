from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection, url_valid, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock,
        connection: bool,
        url_valid: bool,
        expected_result: str
) -> None:
    mock_has_internet_connection.return_value = connection
    mock_valid_google_url.return_value = url_valid
    assert can_access_google_page("https://mate.academy") == expected_result
