from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page(
    valid_url: mock, has_net_con: mock
) -> None:
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_valid_url_no_internet_connection(
    valid_url: mock, has_net_con: mock
) -> None:
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_invalid_url_has_internet_connection(
    valid_url: mock, has_net_con: mock
) -> None:
    assert can_access_google_page("https://www4*#8539.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=False)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_invalid_url_and_no_internet_connection(
    valid_url: mock, has_net_con: mock
) -> None:
    assert can_access_google_page("https://www4*#8539.com") == "Not accessible"
