import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        valid_url: bool,
        internet_connection: bool,
        expected_result: str
) -> None:
    with mock.patch.multiple(
            "app.main",
            valid_google_url=mock.Mock(return_value=valid_url),
            has_internet_connection=mock.Mock(return_value=internet_connection)
    ):
        result = can_access_google_page("https://www.google.com")
        assert result == expected_result
