from app.main import can_access_google_page
from unittest.mock import patch


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(
        mock_internet: patch,
        mock_valid_url: patch
) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = True

    assert (can_access_google_page("https://www.google.com")
            == "Accessible"), (
        "Should be accessible when URL is valid"
        "and there is an internet connection."
    )


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_no_internet(
        mock_internet: patch,
        mock_valid_url: patch
) -> None:
    mock_internet.return_value = False
    mock_valid_url.return_value = True

    assert (can_access_google_page("https://www.google.com")
            == "Not accessible"), (
        "Should be 'Not accessible' because there is no internet connection,"
        "even though the URL is valid."
    )


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_invalid_url(
        mock_internet: patch,
        mock_valid_url: patch
) -> None:
    mock_internet.return_value = True
    mock_valid_url.return_value = False

    assert (can_access_google_page("https://www.invalid-url.com")
            == "Not accessible"), (
        "Should be 'Not accessible' because the URL is invalid,"
        "even though there is an internet connection."
    )


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_no_internet_and_invalid_url(
        mock_internet: patch,
        mock_valid_url: patch
) -> None:
    mock_internet.return_value = False
    mock_valid_url.return_value = False

    assert (can_access_google_page("https://www.invalid-url.com")
            == "Not accessible"), (
        "Should be 'Not accessible' because both the URL is invalid"
        "and there is no internet connection."
    )
