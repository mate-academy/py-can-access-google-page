import pytest
from unittest.mock import patch, Mock, MagicMock
from .main import (can_access_google_page,
                   has_internet_connection,
                   valid_google_url)


GOOGLE_URL: str = "https://www.google.com/"


@pytest.mark.parametrize("status_code, expected", [(200, True), (404, False)])
def test_valid_google_url(status_code: int, expected: bool) -> None:
    with patch("requests.get") as mock_get:
        mock_response = Mock(status_code=status_code)
        mock_get.return_value = mock_response
        assert valid_google_url(GOOGLE_URL) is expected


@pytest.mark.parametrize("hour, expected", [(12, True), (2, False)])
def test_has_internet_connection(hour: int, expected: bool) -> None:
    with patch("datetime.datetime") as mock_datetime:
        mock_now = MagicMock(hour=hour)
        mock_datetime.now.return_value = mock_now
        assert has_internet_connection() is expected


@pytest.mark.parametrize(
    "has_connection, valid_url, expected",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
    has_connection: bool, valid_url: bool, expected: str
) -> None:
    with patch(
            "app.main.has_internet_connection", return_value=has_connection
    ), patch("app.main.valid_google_url", return_value=valid_url):
        assert can_access_google_page(GOOGLE_URL) == expected
