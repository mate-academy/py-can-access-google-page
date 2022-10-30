import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url() -> None:
    with mock.patch("app.main.valid_google_url") \
            as mock_valid_url:
        yield mock_valid_url


@pytest.fixture()
def mock_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") \
            as mock_connection:
        yield mock_connection


def test_true_if_valid_url_and_has_connection(
        mock_valid_google_url: mock,
        mock_internet_connection: mock) -> None:
    mock_valid_google_url.return_value = True
    mock_internet_connection.return_value = True

    assert can_access_google_page("www.facebook.com") == "Accessible", (
        "It is accessible when URL is valid and there is internet connection!"
    )


def test_test_cannot_access_if_only_valid_url(
        mock_valid_google_url: mock,
        mock_internet_connection: mock) -> None:

    mock_valid_google_url.return_value = True
    mock_internet_connection.return_value = False

    assert can_access_google_page("www.facebook.com") == "Not accessible", (
        "Can't access the page as there is no internet connection"
    )


def test_cannot_access_if_only_connection(
        mock_valid_google_url: mock,
        mock_internet_connection: mock) -> None:

    mock_valid_google_url.return_value = False
    mock_internet_connection.return_value = True

    assert can_access_google_page("www.facebook.com") == "Not accessible", (
        "Can't access the page as URL address is not valid"
    )


def test_cannot_access_not_valid_url_and_no_connection(
        mock_valid_google_url: mock,
        mock_internet_connection: mock) -> None:

    mock_valid_google_url.return_value = False
    mock_internet_connection.return_value = False

    assert can_access_google_page("www.facebook.com") == "Not accessible", (
        "Can't access the page as URL address is not valid"
        "and no internet connection"
    )
