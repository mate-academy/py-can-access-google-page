import pytest
from app.main import can_access_google_page
from unittest.mock import patch


@pytest.mark.parametrize(
    "mocked_connection, mocked_url, result",
    [
        (True, True, "Accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
    ],
)
def test_can_access_google_page(mocked_connection: bool,
                                mocked_url: bool, result: str) -> None:
    with patch("app.main.has_internet_connection",
               return_value=mocked_connection), patch("app.main.valid_google_url", return_value=mocked_url):
        assert can_access_google_page("https://www.google.com") == result
