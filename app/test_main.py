import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "connection_status, url_status, access_status",
    [
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (True, True, "Accessible")
    ],
    ids=[
        "When you don`t have internet connection - site is not accessible",
        "When page is offline - site is not accessible",
        "When you have internet connection and page is online "
        "- you have access to site"
    ]
)
def test_can_access_to_google_page(
        connection_status: bool,
        url_status: bool,
        access_status: str
) -> None:
    with (mock.patch("app.main.has_internet_connection") as mocked_connection,
          mock.patch("app.main.valid_google_url") as mocked_url):
        mocked_connection.return_value = connection_status
        mocked_url.return_value = url_status
        assert (can_access_google_page("https://www.google.com/")
                == access_status)
