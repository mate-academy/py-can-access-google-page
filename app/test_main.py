from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_url: mock.Mock,
        mock_internet: mock.Mock,
        internet: bool,
        valid_url: bool,
        result: str) -> None:
    mock_internet.return_value = internet
    mock_valid_url.return_value = valid_url
    assert can_access_google_page("https://www.google.com") == result
