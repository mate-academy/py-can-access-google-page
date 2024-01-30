import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, connection, expected, test_id",
    [
        (True, True, "Accessible", "if all conditions are acceptable"),
        (True, False, "Not accessible", "if only url is acceptable"),
        (False, True, "Not accessible", "if only connection is acceptable"),
        (False, False, "Not accessible", "if both are unacceptable")
    ]
)
def test_can_access_google_page(
        url: str,
        connection: bool,
        expected: str,
        test_id: str
) -> None:
    with mock.patch.multiple(
            "app.main",
            valid_google_url=mock.MagicMock(return_value=url),
            has_internet_connection=mock.MagicMock(return_value=connection)
    ):
        assert can_access_google_page(url) == expected
