from .main import can_access_google_page
from unittest import mock
from typing import Callable


def test_try_to_connect_ok() -> None:
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_try_to_check_url_is_false_connect_true(
        mocked_valid_url: Callable,
        mock_internet: Callable
) -> None:
    mocked_valid_url.return_value = False
    mock_internet.return_value = True

    assert can_access_google_page("https://www.google") == "Not accessible"

    mocked_valid_url.assert_called
    mock_internet.assert_called


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_try_to_check_url_is_true_connect_false(
        mocked_valid_url: Callable,
        mock_internet: Callable
) -> None:
    mocked_valid_url.return_value = True
    mock_internet.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"

    mocked_valid_url.assert_called
    mock_internet.assert_called


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_try_to_check_url_is_false_connect_false(
        mocked_valid_url: Callable,
        mock_internet: Callable
) -> None:
    mocked_valid_url.return_value = False
    mock_internet.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"

    mocked_valid_url.assert_called
    mock_internet.assert_called


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_try_to_check_url_is_true_connect_true(
        mocked_valid_url: Callable,
        mock_internet: Callable
) -> None:
    mocked_valid_url.return_value = True
    mock_internet.return_value = True

    assert can_access_google_page("https://www.google.com") == "Accessible"

    mocked_valid_url.assert_called
    mock_internet.assert_called
