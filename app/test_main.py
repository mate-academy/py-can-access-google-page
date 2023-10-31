from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_google_url_value, has_internet_connection_value, expected",
    [
        pytest.param(
            "http://www.google.com",
            True,
            True,
            "Accessible",
            id="should return accessible when page is valid "
               "and has internet connection"
        ),
        pytest.param(
            "http:////n.com",
            False,
            True,
            "Not accessible",
            id="should return not accessible when page "
               "is not valid and has internet connection"
        ),
        pytest.param(
            "http://www.google.com",
            True,
            False,
            "Not accessible",
            id="should return not accessible when page is valid "
               "and doesn't have internet connection"
        ),
        pytest.param(
            "http://www.badexample.com",
            False,
            False,
            "Not accessible",
            id="should return not accessible when page is not valid "
               "and doesn't have internet connection"
        )
    ]
)
def test_can_access_google_page(
        url: str,
        valid_google_url_value: bool,
        has_internet_connection_value: bool,
        expected: str
) -> None:
    with mock.patch("app.main.valid_google_url",
                    return_value=valid_google_url_value), \
         mock.patch("app.main.has_internet_connection",
                    return_value=has_internet_connection_value):
        assert can_access_google_page(url) == expected
