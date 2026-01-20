from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import (can_access_google_page)


@mock.patch("app.main.valid_google_url")
def test_has_internet_connection_is_called_ok(mock_has_internet_connection:
                                              MagicMock) -> None:
    can_access_google_page("valid_url")
    mock_has_internet_connection.assert_called_once()


@pytest.mark.parametrize(
    "is_url_ok,is_connection_ok,result",
    [
        pytest.param(True, True, "Accessible",
                     id="url and connection are ok"),
        pytest.param(True, False, "Not accessible",
                     id="url and connection are ok"),
        pytest.param(False, True, "Not accessible",
                     id="url and connection are ok"),
        pytest.param(False, False, "Not accessible",
                     id="url and connection are ok"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock,
        result: str,
        is_connection_ok: bool,
        is_url_ok: bool) -> None:
    mock_valid_google_url.return_value = is_url_ok
    mock_has_internet_connection.return_value = is_connection_ok
    assert can_access_google_page("valid_url") == result
