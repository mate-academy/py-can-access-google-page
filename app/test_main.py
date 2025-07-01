from unittest.mock import patch

from app.main import can_access_google_page


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_success(mock_internet: bool,
                                        mock_url: bool) -> None:
    assert can_access_google_page("https://www.google.com") == "Accessible"


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=False)
def test_can_access_google_page_invalid_url(mock_internet: bool,
                                            mock_url: bool) -> None:
    assert can_access_google_page("https://not-google.com") == "Not accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_no_internet(mock_internet: bool,
                                            mock_url: bool) -> None:
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=False)
def test_can_access_google_page_both_invalid(mock_internet: bool,
                                             mock_url: bool) -> None:
    assert can_access_google_page("https://fakeurl.com") == "Not accessible"
