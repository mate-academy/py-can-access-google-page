from unittest import mock


from app.main import (can_access_google_page)


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page(mock_internet: bool, mock_valid: bool) -> None:
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_no_valid(mock_internet: bool,
                                         mock_valid: bool) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_no_connection(mock_internet: bool,
                                              mock_valid: bool) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"
