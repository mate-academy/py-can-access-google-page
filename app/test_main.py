import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture
def mock_has_internet() -> mock.MagicMock:
    with mock.patch("app.main.has_internet_connection") as mocked:
        yield mocked


@pytest.fixture
def mock_valid_url() -> mock.MagicMock:
    with mock.patch("app.main.valid_google_url") as mocked:
        yield mocked


def test_if_both_true(
        mock_valid_url: mock.MagicMock,
        mock_has_internet: mock.MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = True
    assert (can_access_google_page("https://www.google.com/")
            == "Accessible")


def test_if_both_false(
        mock_valid_url: mock.MagicMock,
        mock_has_internet: mock.MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = False
    assert (can_access_google_page("https://www.google.com/")
            == "Not accessible")


def test_if_valid_true(
        mock_valid_url: mock.MagicMock,
        mock_has_internet: mock.MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_has_internet.return_value = False
    assert (can_access_google_page("https://www.google.com/")
            == "Not accessible")


def test_if_connection_true(
        mock_valid_url: mock.MagicMock,
        mock_has_internet: mock.MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True
    assert (can_access_google_page("https://www.google.com/")
            == "Not accessible")
