from unittest.mock import patch, Mock

from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_with_valid_url_and_connection(
    mock_internet: Mock, mock_valid_url: Mock
) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = True

    actual_result = can_access_google_page("https://google.com")

    assert actual_result == "Accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_with_valid_url_and_connection(
    mock_internet: Mock, mock_valid_url: Mock
) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = False

    actual_result = can_access_google_page("https://google.com")

    assert actual_result == "Not accessible"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_with_valid_url_and_no_connection(
    mock_internet: Mock, mock_valid_url: Mock
) -> None:
    mock_internet.return_value = False
    mock_valid_url.return_value = True

    actual_result = can_access_google_page("https://google.com")

    assert actual_result == "Not accessible"



@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_with_invalid_url_and_no_connection(
    mock_internet: Mock, mock_valid_url: Mock
) -> None:
    mock_internet.return_value = False
    mock_valid_url.return_value = False

    actual_result = can_access_google_page("https://google.com")

    assert actual_result == "Not accessible"
