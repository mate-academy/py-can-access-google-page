from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, connection, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "if all conditions are acceptable",
        "if only url is acceptable",
        "if only connection is acceptable",
        "if both are unacceptable"
    ]
)
def test_can_access_google_page(
        url: str,
        connection: bool,
        expected: str
) -> None:
    with mock.patch.multiple(
            "app.main",
            valid_google_url=mock.MagicMock(return_value=url),
            has_internet_connection=mock.MagicMock(return_value=connection)
    ):
        assert can_access_google_page(url) == expected
