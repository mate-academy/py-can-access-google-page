from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.fixture()
def url() -> str:
    return "https://www.google.com"


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page(
        mock_valid: bool,
        mock_internet: bool,
        url: str) -> None:
    assert can_access_google_page(url) == "Accessible"


@mock.patch("app.main.has_internet_connection", return_value=False)
def test_can_not_access_google_page_no_internet(
        mock_internet: bool,
        url: str) -> None:
    assert can_access_google_page(url) == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_not_access_google_page_no_valid_url(
        mock_internet: bool,
        mock_valid: bool,
        url: str) -> None:
    assert can_access_google_page(url) == "Not accessible"


@mock.patch("app.main.has_internet_connection", return_value=True)
@mock.patch("app.main.valid_google_url", return_value=False)
def test_can_not_access_google_page_only_with_internet(
        mock_valid: bool,
        mock_internet: bool,
        url: str) -> None:
    assert can_access_google_page(url) == "Not accessible"
