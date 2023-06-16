from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, res_valid_google_url, res_internet_connection, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.google.com", False, True, "Not accessible"),
        ("https://www.google.com", False, False, "Not accessible"),

    ],
    ids=[
        "Should return 'Accessible' when all functions = True",
        "Should return 'Not accessible' when res_valid_google_url = False",
        "Should return 'Not accessible' when res_internet_connection = False",
        "Should return 'Not accessible' when all functions = False",
    ]
)
def test_valid_url_and_connection_exists(
        url: str,
        res_valid_google_url: bool,
        res_internet_connection: bool,
        expected: str
) -> None:
    with (mock.patch(
            "app.main.valid_google_url",
            return_value=res_valid_google_url
    ),
        mock.patch(
            "app.main.has_internet_connection",
            return_value=res_internet_connection)
    ):
        assert (can_access_google_page(url)
                == expected)
