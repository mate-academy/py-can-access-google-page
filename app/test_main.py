import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection,valid_google_url,url,access",
    [(False, True, "https://www.google.com", "Not accessible"),
     (True, False, "https://www.gogle.com", "Not accessible"),
     (True, True, "https://www.google.com", "Accessible"),
     (False, False, "google", "Not accessible")]
)
def test_can_access_google_page(
        has_internet_connection: bool,
        valid_google_url: bool,
        url: str,
        access: str
) -> None:
    with (patch("app.main.valid_google_url") as mocked_valid_url,
          patch("app.main.has_internet_connection") as mocked_has_connection):
        mocked_valid_url.return_value = valid_google_url
        mocked_has_connection.return_value = has_internet_connection
        assert can_access_google_page(url) == access
