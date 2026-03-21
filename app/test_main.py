from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection, url, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(connection: bool,
                                url: bool,
                                expected: str
                                ) -> None:
    with (mock.patch("app.main.has_internet_connection",
                     return_value=connection),
          mock.patch("app.main.valid_google_url",
                     return_value=url)):
        assert can_access_google_page("https://google.com") == expected
