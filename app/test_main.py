import pytest
from unittest.mock import patch
from .main import can_access_google_page


@pytest.mark.parametrize(
    "internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page_with_different_scenarios(
        internet: bool, valid_url: bool, expected: str) -> None:
    try:
        with patch("app.main.has_internet_connection", return_value=internet),\
             patch("app.main.valid_google_url", return_value=valid_url):
            assert can_access_google_page("https://www.google.com") == expected
    except Exception as e:
        pytest.fail("Test failed with exception: {}".format(e))
