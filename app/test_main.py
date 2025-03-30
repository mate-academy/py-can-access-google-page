from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url_value, has_internet_connection_value, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_access_google_page(
        valid_google_url_value: bool,
        has_internet_connection_value: bool,
        expected_result: str
) -> None:
    with mock.patch("app.main.valid_google_url",
                    return_value=valid_google_url_value), \
            mock.patch("app.main.has_internet_connection",
                       return_value=has_internet_connection_value):
        result = can_access_google_page("https://www.google.com")
        assert result == expected_result
