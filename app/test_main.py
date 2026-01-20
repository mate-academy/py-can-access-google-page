import pytest
from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_mocked_function_called(
    mocked_has_internet_connection: callable, mocked_valid_google_url: callable
) -> None:
    mocked_has_internet_connection.return_value = True
    mocked_valid_google_url.return_value = True
    can_access_google_page("https://www.google.com.ua/")
    mocked_has_internet_connection.assert_called_once()
    mocked_valid_google_url.assert_called_once()


@pytest.mark.parametrize(
    "url, has_internet_connection_return, valid_google_url_return, result",
    [
        ("https://www.google.com.ua/", True, True, "Accessible"),
        ("https://www.google.com.ua/", True, False, "Not accessible"),
        ("https://www.google.com.ua/", False, True, "Not accessible"),
        ("https://www.google.com.ua/", False, False, "Not accessible"),
    ],
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
    mocked_has_internet_connection: callable,
    mocked_valid_google_url: callable,
    url: str,
    has_internet_connection_return: bool,
    valid_google_url_return: bool,
    result: bool,
) -> None:
    mocked_has_internet_connection.return_value = (
        has_internet_connection_return
    )
    mocked_valid_google_url.return_value = valid_google_url_return
    assert can_access_google_page(url) == result
