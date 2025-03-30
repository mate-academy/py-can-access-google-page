from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, has_connection, is_valid, expected",
    [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.google.com", False, True, "Not accessible"),
        ("https://www.googoo.com", True, False, "Not accessible"),
        ("https://www.googoo.com", False, False, "Not accessible"),
    ],
    ids=[
        "Should return accessible if has connection and url is valid",
        "Should return not accessible if no connection",
        "Should return not accessible if url is not correct",
        "Should return not accessible if url is not correct & no connection",
    ]
)
def test_can_access_google_page(
        url: str,
        has_connection: bool,
        is_valid: bool,
        expected: str) -> None:

    mock_has_connection = mock.Mock(return_value=has_connection)
    mock_valid_google_url = mock.Mock(return_value=is_valid)

    with mock.patch(
            "app.main.valid_google_url", side_effect=mock_valid_google_url
    ), mock.patch(
        "app.main.has_internet_connection", side_effect=mock_has_connection
    ):
        assert can_access_google_page(url) == expected
