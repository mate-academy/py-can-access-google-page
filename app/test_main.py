import pytest
from unittest.mock import MagicMock, patch

from app import main


@pytest.mark.parametrize(
    "valid_url, internet_connection, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_has_internet_connection: MagicMock,
        mocked_valid_google_url: MagicMock,
        valid_url: bool,
        internet_connection: bool,
        expected_result: str
) -> None:
    mocked_valid_google_url.return_value = valid_url
    mocked_has_internet_connection.return_value = internet_connection
    assert main.can_access_google_page("fake_url") == expected_result
