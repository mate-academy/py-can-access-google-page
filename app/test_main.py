from __future__ import annotations

from unittest.mock import patch

import pytest

from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_url_and_connection_is_accessible(
    mocked_valid_google_url,
    mocked_has_internet_connection,
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = True

    assert can_access_google_page("https://www.google.com/") == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_is_not_accessible(
    mocked_valid_google_url,
    mocked_has_internet_connection,
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = True

    assert (
        can_access_google_page("https://www.google.com/")
        == "Not accessible"
    )


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_no_internet_connection_is_not_accessible(
    mocked_valid_google_url,
    mocked_has_internet_connection,
) -> None:
    mocked_valid_google_url.return_value = True
    mocked_has_internet_connection.return_value = False

    assert (
        can_access_google_page("https://www.google.com/")
        == "Not accessible"
    )


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_invalid_url_and_no_connection_is_not_accessible(
    mocked_valid_google_url,
    mocked_has_internet_connection,
) -> None:
    mocked_valid_google_url.return_value = False
    mocked_has_internet_connection.return_value = False

    assert (
        can_access_google_page("https://www.google.com/")
        == "Not accessible"
    )


@pytest.mark.parametrize(
    "url_is_valid, has_connection, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_returns_expected_result(
    mocked_valid_google_url,
    mocked_has_internet_connection,
    url_is_valid: bool,
    has_connection: bool,
    expected: str,
) -> None:
    mocked_valid_google_url.return_value = url_is_valid
    mocked_has_internet_connection.return_value = has_connection

    assert (
        can_access_google_page("https://www.google.com/") == expected
    )
