import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, has_connection, expected",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://google.com", True, False, "Not accessible"),
        ("https://fake.com", False, True, "Not accessible"),
        ("https://fake.com", False, False, "Not accessible"),
    ],
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_url: MagicMock,
    mock_has_connection: MagicMock,
    url: str,
    valid_url: bool,
    has_connection: bool,
    expected: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_has_connection.return_value = has_connection

    assert can_access_google_page(url) == expected
