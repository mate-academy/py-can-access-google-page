from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture
def mocked_dependencies():
    with (
        mock.patch("app.main.has_internet_connection") as mock_conn,
        mock.patch("app.main.valid_google_url") as mock_url
    ):
        yield mock_conn, mock_url


@pytest.fixture
def url_example():
    return "https://google.com/"


def test_valid_url_and_connection_exists(
        mocked_dependencies,
        url_example,
):
    mock_conn, mock_url = mocked_dependencies

    mock_conn.return_value = True
    mock_url.return_value = True

    assert can_access_google_page(url_example) == "Accessible"

    mock_conn.assert_called_once()
    mock_url.assert_called_once_with(url_example)


def test_not_accessible_when_no_internet(
        mocked_dependencies,
        url_example,
):
    mock_conn, mock_url = mocked_dependencies
    mock_conn.return_value = False

    assert can_access_google_page(url_example) == "Not accessible"

    mock_conn.assert_called_once()
    mock_url.assert_not_called()


def test_not_accessible_when_invalid_url(
        mocked_dependencies,
        url_example,
):
    mock_conn, mock_url = mocked_dependencies
    mock_conn.return_value = True
    mock_url.return_value = False

    assert can_access_google_page(url_example) == "Not accessible"

    mock_conn.assert_called_once()
    mock_url.assert_called_once_with(url_example)
