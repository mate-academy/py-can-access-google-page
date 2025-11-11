import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize("url", [
    "https://www.google.com",
])
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_all_true(
    mock_valid_google_url: any,
    mock_has_internet_connection: any,
    url: any
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    assert can_access_google_page(url) == "Accessible"
    mock_valid_google_url.assert_called_with(url)
    mock_has_internet_connection.assert_called_once()


@pytest.mark.parametrize("url", [
    "https://www.gogle.com",
])
@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=False)
def test_can_access_google_page_url_invalid(
    mock_valid_google_url: any,
    mock_has_internet_connection: any,
    url: any
) -> None:
    assert can_access_google_page(url) == "Not accessible"
    mock_valid_google_url.assert_called_with(url)


@pytest.mark.parametrize("url", [
    "https://www.google.com",
])
@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_no_internet(
    mock_valid_google_url: any,
    mock_has_internet_connection: any,
    url: any
) -> None:
    assert can_access_google_page(url) == "Not accessible"
    mock_valid_google_url.assert_not_called()


@pytest.mark.parametrize("url", [
    "https://www.google.com",
])
@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=False)
def test_can_access_google_page_all_falses(
    mock_valid_google_url: any,
    mock_has_internet_connection: any,
    url: any
) -> None:
    assert can_access_google_page(url) == "Not accessible"
    mock_valid_google_url.assert_not_called()
