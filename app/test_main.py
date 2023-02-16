from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access(valid_url, has_connection) -> None:
    assert can_access_google_page("https://www.google.com/") == "Accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_not_access_invalid_url(valid_url, has_connection) -> None:
    assert can_access_google_page("https://www.go73736to") == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_can_not_access_no_connection(valid_url, has_connection) -> None:
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_can_not_access(valid_url, has_connection) -> None:
    assert can_access_google_page("https://www.goohgfhfhf") == "Not accessible"
