from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def url_name() -> str:
    return "http://google.com.ua"


@mock.patch("app.main.has_internet_connection")
def test_called_func_has_internet_connection(
        mocked_has_internet_connection: mock, url_name: str
) -> None:
    can_access_google_page(url_name)
    mocked_has_internet_connection.assert_called_once()


@mock.patch("app.main.valid_google_url")
def test_called_func_valid_google_url(
        mocked_valid_google_url: mock, url_name: str
) -> None:
    can_access_google_page(url_name)
    mocked_valid_google_url.assert_called_once_with(url_name)
