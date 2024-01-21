import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "link, valid_url_value, has_connection_value, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://fee.com", False, True, "Not accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://fee.com", False, False, "Not accessible"),
    ],
    ids=[
        "can_access_google_page",
        "not valid url",
        "no connection",
        "both invalid"
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        has_connection: mock.MagicMock,
        valid_url: mock.MagicMock,
        link: str,
        valid_url_value: bool,
        has_connection_value: bool,
        expected: str
) -> None:
    valid_url.return_value = valid_url_value
    has_connection.return_value = has_connection_value

    assert can_access_google_page(link) == expected
