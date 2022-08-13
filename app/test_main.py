from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
def test_valid_google_url_true(mocked_result_valid):
    mocked_result_valid.return_value = True
    result = can_access_google_page("https://google.com/")
    assert result == "Accessible"


@mock.patch("app.main.valid_google_url")
def test_valid_google_url_false(mocked_result_valid):
    mocked_result_valid.return_value = False
    result = can_access_google_page("http://allfuses.com/")
    assert result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection_true(mocked_result_valid):
    mocked_result_valid.return_value = True
    result = can_access_google_page("https://google.com/")
    assert result == "Accessible"


@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection_false(mocked_result_valid):
    mocked_result_valid.return_value = False
    result = can_access_google_page("https://google.com/")
    assert result == "Not accessible"
