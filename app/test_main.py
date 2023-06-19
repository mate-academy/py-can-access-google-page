from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize("valid_url, internet_connection, answer",
                         [(True, True, "Accessible"),
                          (False, True, "Not accessible"),
                          (True, False, "Not accessible"),
                          (False, False, "Not accessible")],
                         ids=[
                             "url and connect True Accessible",
                             "url False connect True Not accessible",
                             "url True connect False Not accessible",
                             "url and connect False Not accessible"
                         ])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_page(url: bool, connect: bool, valid_url: bool,
                     internet_connection:
                     bool, answer: str) -> None:
    url.return_value = valid_url
    connect.return_value = internet_connection
    assert can_access_google_page("https://www.freecodecamp.org") == answer
