import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, internet_connection, result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ]
)
def test_access_google_page(
        url: bool,
        internet_connection: bool,
        result: str
) -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connect, \
            mock.patch("app.main.valid_google_url") as mocked_url:
        mocked_connect.return_value = internet_connection
        mocked_url.return_value = url
        assert can_access_google_page("https://www.google.com") == result
