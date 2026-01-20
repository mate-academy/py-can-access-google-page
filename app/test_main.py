from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "test_url,valid_url,has_internet_connection,expected_result",
    [
        ("https://www.google.com/", True, True, "Accessible"),
        ("https://www.google.com/", True, False, "Not accessible"),
        ("https://mate.academy/", False, True, "Not accessible"),
        ("https://mate.academy/", False, False, "Not accessible")
    ]
)
def test_can_access_google_page(
        test_url: str,
        valid_url: bool,
        has_internet_connection: bool,
        expected_result: str
) -> None:
    with (mock.patch("app.main.valid_google_url",
                     return_value=valid_url),
          mock.patch("app.main.has_internet_connection",
                     return_value=has_internet_connection)):
        assert can_access_google_page(test_url) == expected_result


def test_internal_functions_called_only_once() -> None:
    with (mock.patch("app.main.valid_google_url") as valid_url,
          mock.patch("app.main.has_internet_connection") as connection):

        can_access_google_page("https://www.google.com/")

        connection.assert_called_once()
        valid_url.assert_called_once()
