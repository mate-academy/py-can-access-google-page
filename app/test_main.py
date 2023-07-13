from unittest import mock

from app.main import (
    valid_google_url,
    can_access_google_page
)


@mock.patch("requests.get")
def test_valid_google_url(mocked_request: any) -> None:
    valid_google_url("")

    mocked_request.assert_called_once()


@mock.patch("app.main.valid_google_url")
def test_valid_google_url_works_in_can_access_google_page(
        mocked_valid_url: any
) -> None:
    can_access_google_page("http://google.com")

    mocked_valid_url.assert_called_once()


@mock.patch("app.main.has_internet_connection")
def test_has_internet_connection_works_in_can_access_google_page(
        mock_internet_connection: any
) -> None:
    can_access_google_page("http://google.com")

    mock_internet_connection.assert_called_once()
