import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, internet_connection, result",
    [
        ("http://www.google.com", True, True, "Accessible"),
        ("http://www.notexistpage.com", False, False, "Not accessible"),
        ("http://www.google.com", True, False, "Not accessible"),
        ("http://www.notexistpage.com", False, True, "Not accessible"),
    ],
    ids=[
        "True/True valid_url/has_internet_connection must be Accessible",
        "False/False valid_url/has_internet_connection must be Not accessible",
        "True/False valid_url/has_internet_connection must be Not accessible",
        "False/True valid_url/has_internet_connection must be Not accessible",
    ]
)
def test_can_access_google_page(
        url: str,
        valid_url: bool,
        internet_connection: bool,
        result: str
) -> None:
    with (mock.patch("app.main.valid_google_url") as vld_url,
          mock.patch("app.main.has_internet_connection") as intrnt_connection):
        vld_url.return_value = valid_url
        intrnt_connection.return_value = internet_connection
        assert can_access_google_page(url) == result
