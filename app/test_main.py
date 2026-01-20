import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, has_internet, excepted",
    [
        ("http://www.google.com", True, True, "Accessible"),
        ("http://www.google.com", True, False, "Not accessible"),
        ("http://www.invalid_url.com", False, True, "Not accessible"),
        ("http://www.invalid_url.com", False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet: bool,
        mock_valid_url: bool,
        url: str,
        valid_url: bool,
        has_internet: bool,
        excepted: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_has_internet.return_value = has_internet
    assert can_access_google_page(url) == excepted
