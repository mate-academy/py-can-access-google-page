from app.main import can_access_google_page
from unittest.mock import patch
import pytest


@pytest.mark.parametrize(
    "valid_url, connection, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_access_google_page(valid_url: bool,
                            connection: bool,
                            expected: str) -> None:
    with (patch("app.main.valid_google_url", return_value=valid_url),
          patch("app.main.has_internet_connection", return_value=connection)):
        result = can_access_google_page("https://www.google.com")
    assert result == expected
