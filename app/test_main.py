import pytest

from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
def test_valid_connection(mocked_connection):
    can_access_google_page("https://www.python.org")
    mocked_connection.assert_called_once()

@mock.patch("app.main.valid_google_url")
def test_valid_url(mocked_url):
    can_access_google_page("https://www.python.org")
    mocked_url.assert_called_once_with("https://www.python.org")
