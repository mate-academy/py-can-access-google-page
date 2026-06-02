from app.main import can_access_google_page
from unittest.mock import patch


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_valid_google_url_and_has_connection(mock_connection : bool,
                                             mock_url: bool) -> bool:
    assert can_access_google_page("google_url") == "Accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_invalid_google_url_and_has_connection(mock_connection : bool,
                                               mock_url: bool) -> bool:
    assert can_access_google_page("google_url") == "Not accessible"


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_valid_google_url_and_no_connection(mock_connection : bool,
                                            mock_url: bool) -> bool:
    assert can_access_google_page("google_url") == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=False)
def test_invalid_google_url_and_no_connection(mock_connection : bool,
                                              mock_url: bool) -> bool:
    assert can_access_google_page("google_url") == "Not accessible"
