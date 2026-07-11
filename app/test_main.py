from unittest import mock
import requests
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url_return, internet_return, get_side_effect, response_status, expected",
    [
        ("https://google.com", True, True, None, 200, "Accessible"),
        ("https://invalid-url.com", False, True, None, None, "Not accessible"),
        ("https://google.com", True, False, None, None, "Not accessible"),
        ("https://google.com", True, True, requests.RequestException, None, "Not accessible"),
    ]
)
@mock.patch("app.main.requests.get")
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_valid_url: mock.MagicMock,
        mock_internet: mock.MagicMock,
        mock_get: mock.MagicMock,
        url: str,
        valid_url_return: bool,
        internet_return: bool,
        get_side_effect: Exception | None,
        response_status: int | None,
        expected: str
) -> None:
    mock_valid_url.return_value = valid_url_return
    mock_internet.return_value = internet_return

    if get_side_effect:
        mock_get.side_effect = get_side_effect
    else:
        mock_get.side_effect = None
        mock_response = mock.MagicMock()
        mock_response.status_code = response_status
        mock_get.return_value = mock_response

    assert can_access_google_page(url) == expected