from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, connection, expected",
    [
        pytest.param(
            True, True, "Accessible",
            id="Access granted"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="Access denied"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="Access denied"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="Access denied"
        )

    ]
)
def test_can_access_google_page(
        url: str,
        connection: bool,
        expected: str
) -> None:

    with (
        mock.patch("app.main.valid_google_url") as mocked_url,
        mock.patch("app.main.has_internet_connection")
        as mocked_has_internet_connection
    ):
        mocked_url.return_value = url
        mocked_has_internet_connection.return_value = connection
        result = can_access_google_page(url)
        assert result == expected, (
            f"Expected result {expected}, "
            f"but got{result}"
        )
