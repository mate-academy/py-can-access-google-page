import pytest

from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, mocked_valid_return, mocked_internet_return, expected",
    [
        ("https://google.com", True, True, "Accessible"),
        ("https://incorrect.com", False, True, "Not accessible"),
    ],
    ids=[
        "valid_url_with_internet",
        "invalid_url_with_internet"
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid: MagicMock,
        mock_internet: MagicMock,
        url: str,
        mocked_valid_return: bool,
        mocked_internet_return: bool,
        expected: str
) -> None:
    mock_valid.return_value = mocked_valid_return
    mock_internet.return_value = mocked_internet_return
    result = can_access_google_page(url)
    assert result == expected

    mock_internet.assert_called_once()
    mock_valid.assert_called_once_with(url)
