from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_cant_access_google_page_if_all_false(
        valid_google_url: bool,
        has_internet_connection: bool) -> None:
    assert can_access_google_page("google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_if_all_true(
        valid_google_url: bool,
        has_internet_connection: bool) -> None:
    assert can_access_google_page("google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_cant_access_google_page_if_internet_is_false(
        valid_google_url: bool,
        has_internet_connection: bool) -> None:
    assert can_access_google_page("google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_cant_access_google_page_if_url_is_false(
        valid_google_url: bool,
        has_internet_connection: bool) -> None:
    assert can_access_google_page("google.com") == "Not accessible"
