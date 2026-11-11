from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_connected,is_valid_url,expected",
    [
        pytest.param(
            True, True, "Accessible",
            id="accessible_when_connection_and_valid_url",
        ),
        pytest.param(
            True, False, "Not accessible",
            id="not_accessible_when_only_connection",
        ),
        pytest.param(
            False, True, "Not accessible",
            id="not_accessible_when_only_valid_url",
        ),
        pytest.param(
            False, False, "Not accessible",
            id="not_accessible_without_connection_and_valid_url",
        ),
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_has_connection: mock.MagicMock,
        mocked_valid_url: mock.MagicMock,
        is_connected: bool,
        is_valid_url: bool,
        expected: str,
) -> None:
    mocked_has_connection.return_value = is_connected
    mocked_valid_url.return_value = is_valid_url

    assert can_access_google_page("https://www.google.com") == expected
