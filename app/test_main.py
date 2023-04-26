import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mock_time_hour() -> bool:
    with mock.patch("app.main.has_internet_connection") as mock_time_hour:
        yield mock_time_hour


@pytest.fixture()
def mock_valid_url() -> bool:
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


url = "https://www.youtube.com"


def test_server_connection_accessible(
        mock_time_hour: bool,
        mock_valid_url: bool
) -> None:
    mock_valid_url.return_value = True
    mock_time_hour.return_value = True
    assert can_access_google_page(url) == "Accessible"


def test_server_connection_not_accessible(
        mock_time_hour: bool,
        mock_valid_url: bool
) -> None:
    mock_valid_url.return_value = False
    mock_time_hour.return_value = True
    assert can_access_google_page(url) == "Not accessible"

    mock_valid_url.return_value = True
    mock_time_hour.return_value = False
    assert can_access_google_page(url) == "Not accessible"

    mock_valid_url.return_value = False
    mock_time_hour.return_value = False
    assert can_access_google_page(url) == "Not accessible"
