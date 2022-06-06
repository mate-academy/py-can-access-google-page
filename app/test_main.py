import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_connection, url, expected",
    [
        (True, True, " http://google.com", "Accessible"),
        (True, False, "http://google.com", "Not accessible"),
        (False, False, "http://12wqewq421321.com", "Not accessible"),
        (False, True, "http://12wqewq421321.com", "Not accessible"),
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_main(
        url_mocker,
        connection_mocker,
        valid_url,
        has_connection,
        url,
        expected
):
    url_mocker.return_value = valid_url
    connection_mocker.return_value = has_connection

    assert can_access_google_page(url) == expected
