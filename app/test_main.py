from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_url() -> mock.Mock:
    with mock.patch("app.main.valid_google_url") as mocked_valid_url:
        yield mocked_valid_url


@pytest.fixture()
def mock_has_internet() -> mock.Mock:
    with mock.patch("app.main.has_internet_connection") as mocked_has_internet:
        yield mocked_has_internet


def test_valid_url_and_connection_exist(
        mock_valid_url: mock.Mock,
        mock_has_internet: mock.Mock
) -> None:

    mock_valid_url.return_value = True
    mock_has_internet.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Accessible"


def test_invalid_url_and_no_internet(
        mock_valid_url: mock.Mock,
        mock_has_internet: mock.Mock
) -> None:

    mock_valid_url.return_value = False
    mock_has_internet.return_value = False

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


def test_invalid_url_and_connection_exist(
        mock_valid_url: mock.Mock,
        mock_has_internet: mock.Mock
) -> None:

    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"


def test_valid_url_and_no_internet(
        mock_valid_url: mock.Mock,
        mock_has_internet: mock.Mock
) -> None:

    mock_valid_url.return_value = True
    mock_has_internet.return_value = False

    result = can_access_google_page("https://www.google.com")

    assert result == "Not accessible"
