from typing import Callable

from unittest import mock

from app.main import can_access_google_page


@mock.patch("requests.get")
def test_not_valid_url_has_internet_connection(
        mock_get: Callable
) -> None:
    mock_response = mock_get()
    mock_response.status_code = 300
    assert can_access_google_page("https://mate.academy/") == "Not accessible"


@mock.patch("datetime.datetime")
def test_has_internet_connection_not_valid_url(
        mock_datetime: Callable
) -> None:
    mock_datetime = mock_datetime()
    mock_datetime.now.return_value.hour = 5
    assert can_access_google_page("https://mate.academy/") == "Not accessible"
