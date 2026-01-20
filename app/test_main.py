from typing import Any
from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_url: Any, mock_internet: Any) -> None:

    mock_url.return_value = True
    mock_internet.return_value = True
    assert can_access_google_page("http://google.com") == "Accessible"

    mock_url.return_value = False
    mock_internet.return_value = True
    assert can_access_google_page("http://google.com") == "Not accessible"

    mock_url.return_value = False
    mock_internet.return_value = False
    assert can_access_google_page("http://google.com") == "Not accessible"

    mock_url.return_value = True
    mock_internet.return_value = False
    assert can_access_google_page("http://google.com") == "Not accessible"
