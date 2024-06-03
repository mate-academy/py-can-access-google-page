from app.main import can_access_google_page
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "google_url, internet_connection, result",
    [
        pytest.param(
            True, True, "Accessible",
            id="If you have internet connection and valid url "
               "you can access to google page"
        ),
        pytest.param(
            True, False, "Not accessible",
            id="If you have no internet connection "
               "you can not access to google page"
        ),
        pytest.param(
            False, True, "Not accessible",
            id="If you have invalid url you can not access to google page"
        ),
        pytest.param(
            False, False, "Not accessible",
            id="If you have invalid url and no internet connection "
               "you can not access to google page"
        )
    ]
)
def test_can_access_google_page(
        google_url: bool,
        internet_connection: bool,
        result: str
) -> None:
    with mock.patch("app.main.valid_google_url", google_url):
        with mock.patch("app.main.has_internet_connection",
                        internet_connection):
            assert can_access_google_page("https://www.google.com") == result
