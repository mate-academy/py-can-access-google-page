import pytest
from unittest import mock
from app.main import can_access_google_page
from mock import MagicMock


@pytest.fixture
def mock_valid_google_url() -> MagicMock:
    with (mock.patch("app.main.valid_google_url")
          as mocked_valid_google_url):
        yield mocked_valid_google_url


@pytest.fixture
def mock_has_internet_connection() -> MagicMock:
    with (mock.patch("app.main.has_internet_connection")
          as mocked_has_internet_connection):
        yield mocked_has_internet_connection


def test_can_access_google_page(
        mock_valid_google_url: MagicMock,
        mock_has_internet_connection: MagicMock
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True

    assert (can_access_google_page("https://www.google.com/")
            == "Accessible")

    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True

    assert (can_access_google_page("https://www.[sdfl;dsf].com/")
            == "Not accessible")

    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False

    assert (can_access_google_page("https://www.google.com/")
            == "Not accessible")
