from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_connection, expected",
    [
        pytest.param(True, True, "Accessible"),
        pytest.param(True, False, "Not accessible"),
        pytest.param(False, True, "Not accessible"),
        pytest.param(False, False, "Not accessible")
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mocked_valid_url: mock.MagicMock,
                                mocked_connection: mock.MagicMock,
                                valid_url: bool,
                                has_connection: bool,
                                expected: str) -> None:

    mocked_valid_url.return_value = valid_url
    mocked_connection.return_value = has_connection
    assert can_access_google_page("") == expected
