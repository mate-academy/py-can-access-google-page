import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.fixture()
def mock_url() -> None:
    with mock.patch("app.main.valid_google_url") as mocked_url:
        yield mocked_url


@pytest.fixture()
def mock_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as mocked_connection:
        yield mocked_connection


def test_true_when_working(mock_url: None,
                           mock_connection: None) -> None:
    mock_url.return_value = True
    mock_connection.return_value = True

    assert can_access_google_page("google.com") == "Accessible", \
        "Can be accessible only with stable internet and valid ulr"


def test_false_with_if_no_internet(mock_url: None,
                                   mock_connection: None) -> None:
    mock_url.return_value = True
    mock_connection.return_value = False

    assert can_access_google_page("google.com") == "Not accessible", \
        "Can not be accessible with no internet connection"


def test_false_if_invalid_url(mock_url: None,
                              mock_connection: None) -> None:
    mock_url.return_value = False
    mock_connection.return_value = True

    assert can_access_google_page("google.com") == "Not accessible", \
        "Can not be accessible with invalid url"


def test_false_when_not_working(mock_url: None,
                                mock_connection: None) -> None:
    mock_url.return_value = False
    mock_connection.return_value = False

    assert can_access_google_page("google.com") == "Not accessible", \
        "Not accessible with no internet and invalid url"
