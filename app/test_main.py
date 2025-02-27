import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, internet, expected",
    [
        ("http://google.com", True, True, "Accessible"),
        ("http://google.com", False, True, "Not accessible"),
        ("http://google.com", True, False, "Not accessible"),
        ("http://google.com", False, False, "Not accessible"),
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_internet: mock,
        mock_valid_url: mock,
        url: str,
        valid_url: bool,
        internet: bool,
        expected: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_internet.return_value = internet

    result = can_access_google_page(url)
    assert result == expected
