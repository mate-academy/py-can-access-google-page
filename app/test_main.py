from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def mock_url():
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mock_connection():
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_should_return_accessible_when_daytime_and_existing_url(
        mock_url,
        mock_connection):

    mock_url.return_value = True
    mock_connection.return_value = True
    assert can_access_google_page("www.youtube.com") == "Accessible"


def test_should_return_not_accessible_when_only_time_is_ok(
        mock_url,
        mock_connection):

    mock_url.return_value = False
    mock_connection.return_value = True
    assert can_access_google_page("www.youtube.com") == "Not accessible"


def test_should_return_not_accessible_when_only_url_is_ok(
        mock_url,
        mock_connection):

    mock_url.return_value = True
    mock_connection.return_value = False
    assert can_access_google_page("www.youtube.com") == "Not accessible"


def test_should_return_not_accessible_when_both_are_not_ok(
        mock_url,
        mock_connection):

    mock_url.return_value = False
    mock_connection.return_value = False
    assert can_access_google_page("www.youtube.com") == "Not accessible"
