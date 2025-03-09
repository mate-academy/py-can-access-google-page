from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_success(
    mock_internet: patch, mock_valid_url: patch
) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible", f"Expected 'Accessible' but got {result}"


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_no_internet(
    mock_internet: patch, mock_valid_url: patch
) -> None:
    mock_internet.return_value = False
    mock_valid_url.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible", (f"Expected 'Not accessible' "
                                        f"but got {result}")


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_invalid_url(
    mock_internet: patch, mock_valid_url: patch
) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = False

    result = can_access_google_page("https://invalid-url.com")

    assert result == "Not accessible", (f"Expected 'Not accessible' "
                                        f"but got {result}")
