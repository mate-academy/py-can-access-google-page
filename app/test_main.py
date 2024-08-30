import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def valid_url():
    with mock.patch("app.main.valid_google_url") as valid_url:
        yield valid_url


@pytest.fixture()
def internet_connection():
    with mock.patch("app.main.has_internet_connection") as internet_connection:
        yield internet_connection


url = "https://google.com"


def test_with_correct_url_and_internet_connection(internet_connection, valid_url):
    valid_url.return_value = True
    internet_connection.return_value = True
    can_access_google_page(url)
    internet_connection.assert_called_once()
    valid_url.assert_called_once_with(url)
    assert can_access_google_page(url) == "Accessible"
