from unittest import mock

from .main import (valid_google_url,
                   has_internet_connection,
                   can_access_google_page)


def test_valid_google_url() -> None:
    assert (
        valid_google_url("https://www.google.com/") is True
    )


def test_has_internet_connection() -> None:
    assert (
        has_internet_connection() is True
    )


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_return_accessible(
    mock_connection: bool, mock_url: str
) -> None:
    mock_connection.return_value = True
    mock_url.return_value = True
    assert (
        can_access_google_page("https://www.google.com/") == "Accessible"
    )


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_return_not_accessible_if_bad_url(
    mock_connection: bool, mock_url: str
) -> None:
    mock_connection.return_value = True
    mock_url.return_value = False
    assert (
        can_access_google_page(
            "https://www.godasavavwqe.com/"
        ) == "Not accessible"
    )


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_return_not_accessible_if_no_connection(
    mock_connection: bool, mock_url: str
) -> None:
    mock_connection.return_value = False
    mock_url.return_value = True
    assert (
        can_access_google_page(
            "https://www.google.com/"
        ) == "Not accessible"
    )
