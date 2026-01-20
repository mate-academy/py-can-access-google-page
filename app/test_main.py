import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet, valid_url, expected",
    [
        ("https://www.google.com/", True, True, "Accessible"),
        ("https://www.google.com/", False, True, "Not accessible"),
        ("https://www.google.com/", True, False, "Not accessible"),
        ("https://www.google.com/", False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_internet_connection(
        mock_internet: mock.Mock,
        mock_valid_url: mock.Mock,
        url: str,
        internet: bool,
        valid_url: bool,
        expected: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_internet.return_value = internet

    assert can_access_google_page(url) == expected
