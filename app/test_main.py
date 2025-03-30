from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_both_true(mock_has_internet: bool, mock_valid_url: bool) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True

    site = can_access_google_page("https://www.google.com/")
    assert site == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_without_internet(mock_has_internet: bool,
                          mock_valid_url: bool) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False

    site = can_access_google_page("https://www.google.com/")
    assert site == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_bad_url(mock_has_internet: bool, mock_valid_url: bool) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    site = can_access_google_page("https://www.bad_url.com/")
    assert site == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_without_is_bad(mock_has_internet: bool, mock_valid_url: bool) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = False

    site = can_access_google_page("https://www.bad-url.com/")
    assert site == "Not accessible"
