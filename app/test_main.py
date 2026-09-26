from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet,valid_url,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    internet: bool,
    valid_url: bool,
    expected: str,
) -> None:
    with (
        mock.patch(
            "app.main.has_internet_connection",
            return_value=internet,
        ),
        mock.patch(
            "app.main.valid_google_url",
            return_value=valid_url,
        ),
    ):
        result = can_access_google_page("https://google.com")

    assert result == expected
