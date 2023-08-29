from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection_status, valid_url, expected",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
    ]
)
def test_can_access_google_page(
        connection_status: bool,
        valid_url: bool,
        expected: str
) -> None:
    with mock.patch("app.main.has_internet_connection",
                    return_value=connection_status):
        with mock.patch("app.main.valid_google_url",
                        return_value=valid_url):
            assert can_access_google_page("http://google.com") == expected
