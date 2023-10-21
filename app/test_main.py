import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_accessible(mock_internet: bool,
                                           mock_url: bool) -> None:
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Accessible"


@patch("app.main.valid_google_url", return_value=True)
@patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_no_internet(mock_internet: bool,
                                            mock_url: bool) -> None:
    url = "https://www.google.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_invalid_url(
    mock_internet: bool,
    mock_url: bool,
) -> None:
    url = "https://invalid-url.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"


@patch("app.main.valid_google_url", return_value=False)
@patch("app.main.has_internet_connection", return_value=False)
def test_can_access_google_page_no_internet_and_invalid_url(
        mock_internet: bool,
        mock_url: bool) -> None:
    url = "https://invalid-url.com"
    result = can_access_google_page(url)
    assert result == "Not accessible"


# Run the tests
if __name__ == "__main__":
    pytest.main()
