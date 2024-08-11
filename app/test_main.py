from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_valid_url_and_connection_exists(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    assert can_access_google_page("http://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_invalid_url(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    assert can_access_google_page("http://kekw") == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_no_internet(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    assert can_access_google_page("http://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_invalid_url_and_no_connection(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool
) -> None:
    assert can_access_google_page("http://kekw") == "Not accessible"
