from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page_when_status_code_200() -> None:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mock_url_response, mock.patch(
        "app.main.has_internet_connection"
    ) as mock_internet_valid:
        mock_url_response.return_value = True
        mock_internet_valid.return_value = True
        assert can_access_google_page(
            url="https://google.com"
        ) == "Accessible"


def test_can_access_google_page_when_status_code_error() -> None:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mock_url_response, mock.patch(
        "app.main.has_internet_connection"
    ) as mock_internet_valid:
        mock_url_response.return_value = False
        mock_internet_valid.return_value = False
        assert can_access_google_page(
            url="https://google.com"
        ) == "Not accessible"


def test_can_access_google_page_when_status_code_200_internet_not() -> None:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mock_url_response, mock.patch(
        "app.main.has_internet_connection"
    ) as mock_internet_valid:
        mock_url_response.return_value = True
        mock_internet_valid.return_value = False
        assert can_access_google_page(
            url="https://google.com"
        ) == "Not accessible"


def test_can_access_google_page_when_status_error_internet_yes() -> None:
    with mock.patch(
            "app.main.valid_google_url"
    ) as mock_url_response, mock.patch(
        "app.main.has_internet_connection"
    ) as mock_internet_valid:
        mock_url_response.return_value = False
        mock_internet_valid.return_value = True
        assert can_access_google_page(
            url="https://google.com"
        ) == "Not accessible"
