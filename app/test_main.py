import pytest
from unittest import mock
from app.main import can_access_google_page
from unittest.mock import MagicMock


@pytest.mark.parametrize(
    "has_internet, is_valid_url, url, expected",
    [
        (True, False, "", "Not accessible"),
        (True, True, "abc", "Accessible"),
        (False, True, "", "Not accessible"),
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_valid_google_url: MagicMock,
    mock_has_internet_connection: MagicMock,
    has_internet: bool,
    is_valid_url: bool,
    url: str,
    expected: str,
) -> None:
    mock_has_internet_connection.return_value = has_internet
    mock_valid_google_url.return_value = is_valid_url

    assert can_access_google_page(url) == expected
