import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet_connection, url_validity, result", [
        ("https://www.google.com/", True, True, "Accessible"),
        ("https://www.google.com/", False, True, "Not accessible"),
        ("https/www.google.c", True, False, "Not accessible"),
        ("https/www.google.c", False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mocked_has_internet_connection: callable,
        mocked_valid_google_url: callable,
        url: str,
        internet_connection: bool,
        url_validity: bool,
        result: bool
) -> None:
    mocked_has_internet_connection.return_value = internet_connection
    mocked_valid_google_url.return_value = url_validity
    assert can_access_google_page(url) == result
