from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page(_: bool, ___: str) -> None:
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_no_internet(_: bool, ___: str) -> None:
    result = can_access_google_page("http://www.google.com")
    assert result == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_cant_access_google_page(_: bool, ___: str) -> None:
    result = can_access_google_page("http://www.google.com")
    assert result == "Not accessible"
