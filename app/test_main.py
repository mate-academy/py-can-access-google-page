from unittest.mock import patch

import pytest

from app.main import can_access_google_page

url = "https://www.notavalidurl.com"


@pytest.mark.parametrize("internet_connection, valid_url, expected_result", [
    (True, True, "Accessible"),
    (False, True, "Not accessible"),
    (True, False, "Not accessible"),
    (False, False, "Not accessible")
], ids=["internet connection - valid URL",
        "no internet connection - valid URL",
        "internet connection - invalid URL",
        "no internet connection - invalid URL"])
def test_can_access_google_page(internet_connection: bool,
                                valid_url: bool,
                                expected_result: str) -> None:
    with patch("app.main.has_internet_connection",
               return_value=internet_connection):
        with patch("app.main.valid_google_url",
                   return_value=valid_url):
            assert can_access_google_page(url) == expected_result
