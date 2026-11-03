from unittest.mock import patch
import pytest

import app.main


@pytest.mark.parametrize(
    "has_internet, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_combinations(
    mock_has_internet: object,
    mock_valid_url: object,
    has_internet: bool,
    valid_url: bool,
    expected: str,
) -> None:
    mock_has_internet.return_value = has_internet
    mock_valid_url.return_value = valid_url

    assert app.main.can_access_google_page("https://google.com") == expected
    mock_has_internet.assert_called_once()
    if has_internet:
        mock_valid_url.assert_called_once_with("https://google.com")


@pytest.mark.parametrize(
    "url",
    [
        "https://google.com",
        "https://www.google.com",
        "https://google.com/search?q=test",
    ],
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page_different_urls(
    mock_has_internet: object,
    mock_valid_url: object,
    url: str,
) -> None:
    mock_has_internet.return_value = True
    mock_valid_url.return_value = True

    assert app.main.can_access_google_page(url) == "Accessible"
    mock_valid_url.assert_called_once_with(url)
