from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_connected,is_valid_url,expected_result",
    [
        pytest.param(
            True, True, "Accessible",
            id="valid connection, valid url"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="invalid connection"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="invalid url"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="invalid connection and invalid url"
        ),
    ]
)
def test_can_access_google_page(
        is_connected: mock,
        is_valid_url: mock,
        expected_result: str
) -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mock_connection,
        mock.patch("app.main.valid_google_url") as mock_valid_url
    ):
        mock_connection.return_value = is_connected
        mock_valid_url.return_value = is_valid_url

        assert can_access_google_page("https://google.com") == expected_result
