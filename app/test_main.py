from unittest.mock import patch
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "mock_valid_google_url_return, "
    "mock_has_internet_connection_return, "
    "expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        mock_valid_google_url_return: bool,
        mock_has_internet_connection_return: bool,
        expected: str
) -> None:
    with (patch("app.main.valid_google_url") as
          mock_valid_google_url,
          patch("app.main.has_internet_connection") as
          mock_has_internet):
        mock_valid_google_url.return_value = mock_valid_google_url_return
        mock_has_internet.return_value = mock_has_internet_connection_return
        assert can_access_google_page("http://www.google.com") == expected
