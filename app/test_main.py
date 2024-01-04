import pytest

from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet,valid_url, url, access",
    [(True, True, "google.com", "Accessible"),
     (False, True, "google.com", "Not accessible"),
     (True, False, "gogle.com", "Not accessible"),
     (False, False, "gogle", "Not accessible")
     ]
)
def test_can_access_google_page(valid_url: bool,
                                has_internet: bool,
                                url: str,
                                access: str) -> None:
    with (patch("app.main.valid_google_url") as mock_valid_url,
          patch("app.main.has_internet_connection") as mock_has_internet):
        mock_valid_url.return_value = valid_url
        mock_has_internet.return_value = has_internet
        assert can_access_google_page(url) == access
