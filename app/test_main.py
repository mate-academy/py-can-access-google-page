from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_valid_url, has_internet, expected",
    [
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible"),
    ],
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_url: mock.MagicMock,
    mock_has_internet: mock.MagicMock,
    is_valid_url: bool,
    has_internet: bool,
    expected: str,
) -> None:
    mock_valid_url.return_value = is_valid_url
    mock_has_internet.return_value = has_internet

    assert can_access_google_page("https://www.google.com") == expected
