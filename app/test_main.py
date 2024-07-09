import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, expected, url",
    [
        (True, True, "Accessible", "https://translate.google.com/"
                                   "?hl=ru&sl=en&tl=ru&op=translate"),
        (False, True, "Not accessible", ""),
        (True, False, "Not accessible", "https://www.python.org/"
                                        "downloads/release/python-3123/"),
        (False, False, "Not accessible", "https://github.com/mate-academy/"
                                         "py-can-access-google-page/pull/956"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: mock.Mock,
        mock_has_internet_connection: mock.Mock,
        valid_url: bool,
        internet_connection: bool,
        expected: str,
        url: str) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_connection

    assert can_access_google_page(url) == expected
