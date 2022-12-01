import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mock_internet_connection() -> None:
    with mock.patch(
            "app.main.has_internet_connection"
    ) as mock_internet_connection:
        yield mock_internet_connection


@pytest.fixture()
def mock_valid_url() -> None:
    with mock.patch("app.main.valid_google_url") as mock_valid_url:
        yield mock_valid_url


def test_access_google_page_when_no_internet(
        mock_internet_connection: mock,
        mock_valid_url: mock
) -> None:
    mock_internet_connection.return_value = False
    mock_valid_url.return_value = True
    assert can_access_google_page(
        "https://www.wikipedia.org/") == "Not accessible"


def test_access_google_page_when_url_not_valid(
        mock_internet_connection: mock,
        mock_valid_url: mock
) -> None:
    mock_internet_connection.return_value = True
    mock_valid_url.return_value = False
    assert can_access_google_page(
        "https://www.wikipedia.org/") == "Not accessible"


def test_accessible_when_internet_and_url_are_ok(
        mock_internet_connection: mock,
        mock_valid_url: mock
) -> None:
    mock_internet_connection.return_value = True
    mock_valid_url.return_value = True
    assert can_access_google_page(
        "https://www.wikipedia.org/") == "Accessible"


def test_accessible_when_internet_and_url_are_not_ok(
        mock_internet_connection: mock,
        mock_valid_url: mock
) -> None:
    mock_internet_connection.return_value = True
    mock_valid_url.return_value = True
    assert can_access_google_page(
        "https://www.wikipedia.org/") == "Accessible"
