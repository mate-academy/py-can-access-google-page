from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    test_cases = [
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible"),
        (True, True, "Accessible")
    ]

    for has_internet_connection, valid_url, expected in test_cases:
        with mock.patch("app.main.has_internet_connection",
                        return_value=has_internet_connection), \
                mock.patch("app.main.valid_google_url",
                           return_value=valid_url):
            assert can_access_google_page("http://google.com") == expected
