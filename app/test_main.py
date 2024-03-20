import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "is_internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page_return_correct_values(
        is_internet: bool,
        valid_url: bool,
        expected: str
) -> None:
    with (
        mock.patch("app.main.has_internet_connection",
                   return_value=is_internet),
        mock.patch("app.main.valid_google_url",
                   return_value=valid_url)
    ):
        assert can_access_google_page("some_str") == expected
