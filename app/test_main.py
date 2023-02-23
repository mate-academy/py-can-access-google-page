from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_access_google_page(url: mock, internet: mock) -> None:
    assert can_access_google_page("https://www.google.com/") == "Accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_with_rong_url_address(url: mock, internet: mock) -> None:
    assert can_access_google_page("https:/www.smorfle.com") == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_with_no_internet_connection(url: mock, internet: mock) -> None:
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_with_no_connection_and_wrong_url(url: mock, internet: mock) -> None:
    assert can_access_google_page("https:/www.smorfle.com") == "Not accessible"
