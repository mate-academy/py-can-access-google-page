import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, has_connection, is_valid, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", False, True, "Not accessible"),
        ("https://www.googoo.com", True, False, "Not accessible"),
    ],
    ids=[
        "Should return accessible if has connection and url is valid",
        "Should return not accessible if no connection",
        "Should return not accessible if url is not correct",
    ]
)
def test_can_access_google_page(
        url: str,
        has_connection: bool,
        is_valid: bool,
        expected: str) -> None:

    def mocked_has_connection(*args) -> bool:
        return has_connection

    def mocked_valid_google_url(*args) -> bool:
        return is_valid

    with mock.patch(
            "app.main.valid_google_url", mocked_valid_google_url
    ), mock.patch(
        "app.main.has_internet_connection", mocked_has_connection
    ):
        assert can_access_google_page(url) == expected
