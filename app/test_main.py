from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_google_url, has_internet_connection, result",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("fake_url", False, True, "Not accessible"),
        ("fake_url", False, False, "Not accessible"),
    ]
)
def test_valid_url_and_connection_exists(
    url: str,
    valid_google_url: str,
    has_internet_connection: bool,
    result: str
) -> None:
    with mock.patch("app.main.valid_google_url",
                    return_value=valid_google_url), \
            mock.patch("app.main.has_internet_connection",
                       return_value=has_internet_connection):
        assert can_access_google_page(url) == result
