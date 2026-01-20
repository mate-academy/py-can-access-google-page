import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def valid_url() -> None:
    with (mock.patch("app.main.valid_google_url")
          as valid_url):
        yield valid_url


@pytest.fixture()
def internet_connection() -> None:
    with (mock.patch("app.main.has_internet_connection")
          as internet_connection):
        yield internet_connection


@pytest.mark.parametrize(
    "url_return_value,connection_return_value,expected",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible")
    ]
)
def test_can_access_google_page_functionality(
        internet_connection: mock,
        valid_url: mock,
        url_return_value: bool,
        connection_return_value: bool,
        expected: str) -> None:

    url = "https://google.com"

    valid_url.return_value = url_return_value
    internet_connection.return_value = connection_return_value
    can_access_google_page(url)
    assert can_access_google_page(url) == expected

    if url_return_value == connection_return_value is True:
        internet_connection.assert_called()
        valid_url.assert_called_with(url)
    else:
        internet_connection.assert_called()
