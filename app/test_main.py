from unittest import mock
from app import main


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(
        mock_internet: bool,
        mock_valid_url: bool
) -> None:

    mock_internet.return_value = True
    mock_valid_url.return_value = True

    assert main.can_access_google_page("https://google.com")


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_not_accessible(
        mock_internet: bool,
        mock_valid: bool
) -> None:
    mock_internet.return_value = False
    mock_valid.return_value = True
    assert (main.can_access_google_page
            ("https://google.com") == "Not accessible")

    mock_internet.return_value = True
    mock_valid.return_value = False

    assert (main.can_access_google_page
            ("https://google.com") == "Not accessible")
