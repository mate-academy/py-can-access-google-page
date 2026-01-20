from unittest import mock
from app.main import can_access_google_page
import pytest


@pytest.mark.parametrize(
    "connection_status,url_status,total_result",
    [
        pytest.param(True, True, "Accessible", id="connection and url True"),
        pytest.param(True, False, "Not accessible", id="missing connection"),
        pytest.param(False, True, "Not accessible", id="missing valid url")
    ]
)
def test_test_main_when_internet_connection_and_valid_url(
        connection_status: bool,
        url_status: bool,
        total_result: str
) -> None:
    with (mock.patch("app.main.has_internet_connection") as connection,
          mock.patch("app.main.valid_google_url") as url):
        connection.return_value = connection_status
        url.return_value = url_status
        assert can_access_google_page("http://www.google.com") == total_result
