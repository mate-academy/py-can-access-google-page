from typing import Any
from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url_value, connection_value, expected_value",
    [
        pytest.param(
            True,
            False,
            "Not accessible",
            id="can not access google page when only valid url"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="can not access google page when only connection exist"
        ),
        pytest.param(
            False,
            False,
            "Not accessible",
            id="can not access google page when no connection and invalid url"
        ),
        pytest.param(
            True,
            True,
            "Accessible",
            id="can access google page when connection exists and valid url"
        )
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mock_test_has_internet_connection: Any,
        mock_test_valid_google_url: Any,
        valid_url_value: str,
        connection_value: str,
        expected_value: str
) -> None:
    mock_test_valid_google_url.return_value = valid_url_value
    mock_test_has_internet_connection.return_value = connection_value

    assert can_access_google_page("http://google.com") == expected_value
