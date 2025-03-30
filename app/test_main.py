from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection, url_is_valid",
    [
        pytest.param(True, True, id="connection exists and url is valid"),
        pytest.param(True, False, id="connection exists but url is invalid"),
        pytest.param(False, True, id="no connection but url is valid"),
        pytest.param(False, False, id="no connection and url is invalid"),
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_returns_valid_results(
    mocked_has_internet_connection: mock.MagicMock,
    mocked_valid_google_url: mock.MagicMock,
    has_connection: bool,
    url_is_valid: bool,
) -> None:
    mocked_has_internet_connection.return_value = has_connection
    mocked_valid_google_url.return_value = url_is_valid

    assert can_access_google_page("http://test.com")

    mocked_has_internet_connection.assert_called_once()
    if has_connection:
        mocked_valid_google_url.assert_called_once_with("http://test.com")
    else:
        mocked_valid_google_url.assert_not_called()
