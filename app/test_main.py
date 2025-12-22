from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_url_and_internet(mock_url: bool, mock_int: bool) -> None:
    mock_url.return_value = True
    mock_int.return_value = True
    assert can_access_google_page("www.mi.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_access_no_url_no_internet(mock_url: bool, mock_int: bool) -> None:
    mock_url.return_value = False
    mock_int.return_value = False
    assert can_access_google_page("www.mi.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_access_no_url(mock_url: bool, mock_int: bool) -> None:
    mock_url.return_value = False
    mock_int.return_value = True
    assert can_access_google_page("www.mi.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_access__no_internet(mock_url: bool, mock_int: bool) -> None:
    mock_url.return_value = True
    mock_int.return_value = False
    assert can_access_google_page("www.mi.com") == "Not accessible"
