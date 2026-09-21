from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_check_when_url_is_valid_and_has_url_connection(
        mock_valid_google_url,
        mock_has_internet_connection
):
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("url") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_check_when_url_is_not_valid_and_has_url_connection(
        mock_valid_google_url,
        mock_has_internet_connection
):
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    assert can_access_google_page("url") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_check_when_url_is_valid_and_has_not_url_connection(
        mock_valid_google_url,
        mock_has_internet_connection
):
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    assert can_access_google_page("url") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_should_check_when_url_is_not_valid_and_has_not_url_connection(
        mock_valid_google_url,
        mock_has_internet_connection
):
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = False

    assert can_access_google_page("url") == "Not accessible"