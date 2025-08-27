import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        valid_google_url: bool,
        has_internet_connection: bool,
        result: str) -> None:

    with (patch("app.main.valid_google_url",
                return_value=valid_google_url),

          patch("app.main.has_internet_connection",
                return_value=has_internet_connection)):

        assert can_access_google_page("https://google.com/") == result
