import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet, valid_url, result",
    [("www.google.com", True, True, "Accessible"),
     ("www.google.com", False, True, "Not accessible"),
     ("www.qwegoogle.com", True, False, "Not accessible"),
     ("www.qwegoogle.com", False, False, "Not accessible")
     ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_is_valid_url_and_connection_exists(
        mock_internet: mock.Mock,
        mock_valid_url: mock.Mock,
        url: str,
        valid_url: bool,
        internet: bool,
        result: str) -> None:
    mock_valid_url.return_value = valid_url
    mock_internet.return_value = internet

    assert can_access_google_page(url) == result
