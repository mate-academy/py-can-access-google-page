import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.fixture
def mocked_network() -> any:
    with (mock.patch("app.main.has_internet_connection") as mock_internet,
          mock.patch("app.main.valid_google_url") as mock_url):
        yield mock_internet, mock_url


def test_can_access_google_page(mocked_network: list) -> None:
    mock_internet, mock_url = mocked_network
    mock_internet.return_value = True
    mock_url.return_value = True
    assert can_access_google_page("any") == "Accessible"


def test_can_not_access_google_page_internet_connection_lost(
        mocked_network: list) -> None:
    mock_internet, mock_url = mocked_network
    mock_internet.return_value = False
    mock_url.return_value = True
    assert can_access_google_page("any") == "Not accessible"


def test_can_not_access_google_page_invalid_google_url(
        mocked_network: list) -> None:
    mock_internet, mock_url = mocked_network
    mock_internet.return_value = True
    mock_url.return_value = False
    assert can_access_google_page("any") == "Not accessible"
