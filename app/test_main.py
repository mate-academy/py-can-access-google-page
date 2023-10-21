from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.fixture()
def valid_google_url_mock():
    with mock.patch("app.main.valid_google_url") as mocked_internet:
        yield mocked_internet


@pytest.fixture()
def mock_has_internet():
    with mock.patch("app.main.has_internet_connection") as mocked_page_url:
        yield mocked_page_url


def test_can_access_google_page(
        valid_google_url_mock,
        mock_has_internet
) -> None:
    valid_google_url_mock.return_value = True
    mock_has_internet.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


def test_return_not_accessible_if_no_internet_connection(
        valid_google_url_mock,
        mock_has_internet
) -> None:
    valid_google_url_mock.return_value = False
    mock_has_internet.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"


def test_return_not_accessible_if_invalid_url(
        valid_google_url_mock,
        mock_has_internet
) -> None:
    valid_google_url_mock.return_value = True
    mock_has_internet.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"
