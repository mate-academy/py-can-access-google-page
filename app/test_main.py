from unittest import mock
import pytest
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
@pytest.mark.parametrize(
    "internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page_scenarios(
    mock_internet: mock.MagicMock,
    mock_valid_url: mock.MagicMock,
    internet: bool,
    valid_url: bool,
    expected: str
) -> None:
    mock_internet.return_value = internet
    mock_valid_url.return_value = valid_url
    result: str = can_access_google_page("https://www.google.com")
    assert result == expected
