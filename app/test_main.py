from unittest.mock import patch

import pytest

from app.main import can_access_google_page

url = "https://www.notavalidurl.com"


@pytest.mark.parametrize("internet, url, expected", [(True,
                                                      True,
                                                      "Accessible"),
                                                     (False, True,
                                                      "Not accessible"),
                                                     (True, False,
                                                      "Not accessible"),
                                                     (False, False,
                                                      "Not accessible")])
def test_can_access_google_page(internet: any,
                                url: str,
                                expected: str) -> None:
    with patch("app.main.has_internet_connection", return_value=internet), \
            patch("app.main.valid_google_url", return_value=url):
        assert can_access_google_page(url) == expected
