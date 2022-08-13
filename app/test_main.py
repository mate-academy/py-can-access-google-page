from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_return_true(mock_valid_url, mock_has_internet):
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True
    assert can_access_google_page("https://some.site.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_return_when_internet_false(mock_valid_url, mock_has_internet):
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False
    assert can_access_google_page("https://some.site.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_return_when_valid_url_false(mock_valid_url, mock_has_internet):
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True
    assert can_access_google_page("https://some.site.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_return_all_false(mock_valid_url, mock_has_internet):
    mock_valid_url.return_value = False
    mock_has_internet.return_value = False
    assert can_access_google_page("https://some.site.com") == "Not accessible"
