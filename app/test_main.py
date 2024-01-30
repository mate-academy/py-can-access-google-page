import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet_connection, expected",
    [(True, True, "Accessible"),
     (True, False, "Not accessible"),
     (False, True, "Not accessible"),
     (False, False, "Not accessible")]
)
def test_can_access_google_page(
        url: str,
        internet_connection: bool,
        expected: str
) -> None:
    with mock.patch("app.main.valid_google_url",
                    return_value=url):
        with mock.patch("app.main.has_internet_connection",
                        return_value=internet_connection):
            assert can_access_google_page(url) == expected
