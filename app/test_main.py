from unittest.mock import MagicMock, patch
import pytest
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "url, mock_valid, mock_internet, expected",
    [
        ("http://google.com", True, True, "Accessible"),
        ("http://google.com", True, False, "Not accessible"),
        ("http://fake.com", False, True, "Not accessible"),
        ("http://fake.com", False, False, "Not accessible"),
    ]
)
def test_valid_url_and_connection_exists_returns_accessible(
    mocked_has_internet: MagicMock,
    mocked_valid: MagicMock,
    url: str,
    mock_valid: bool,
    mock_internet: bool,
    expected: str,
) -> None:
    mocked_valid.return_value = mock_valid
    mocked_has_internet.return_value = mock_internet
    actual = can_access_google_page(url)

    assert actual == expected
    mocked_has_internet.assert_called_once()

    if mock_internet:
        mocked_valid.assert_called_once_with(url)
    else:
        mocked_valid.assert_not_called()
