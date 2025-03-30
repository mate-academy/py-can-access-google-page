import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, valid_url, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_valid_url_and_connection_exists(
    internet_connection: bool,
    valid_url: bool,
    result: str
) -> None:
    with (mock.patch("app.main.valid_google_url",
                     return_value=valid_url),
          mock.patch("app.main.has_internet_connection",
                     return_value=internet_connection)):
        assert can_access_google_page("https://www.google.com") == result
