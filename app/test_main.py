import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection, is_valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    has_connection: bool,
    is_valid_url: bool,
    expected: str,
) -> None:
    with mock.patch(
        "app.main.has_internet_connection",
        return_value=has_connection,
    ), mock.patch(
        "app.main.valid_google_url",
        return_value=is_valid_url,
    ):
        result = can_access_google_page("https://www.google.com")
        assert result == expected
