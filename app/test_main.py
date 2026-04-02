import datetime
from unittest import mock
from app.main import (
    can_access_google_page,
    has_internet_connection,
    valid_google_url,
)


@mock.patch("app.main.requests.get")
def test_valid_google_url(mock_get: mock.MagicMock) -> None:
    mock_get.return_value.status_code = 200
    assert valid_google_url("https://www.google.com") is True

    mock_get.return_value.status_code = 404
    assert valid_google_url("https://www.invalid-url.com") is False


@mock.patch("app.main.datetime")
def test_has_internet_connection(mock_datetime: mock.MagicMock) -> None:
    mock_datetime.datetime.now.return_value = datetime.datetime(
        2024, 1, 1, 6, 0
    )
    assert has_internet_connection() is True

    mock_datetime.datetime.now.return_value = datetime.datetime(
        2024, 1, 1, 23, 0
    )
    assert has_internet_connection() is False


def test_can_access_google_page() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mock_internet,
        mock.patch("app.main.valid_google_url") as mock_valid_url
    ):
        mock_internet: mock.MagicMock
        mock_valid_url: mock.MagicMock

        mock_internet.return_value = True
        mock_valid_url.return_value = True
        assert can_access_google_page("https://www.google.com") == "Accessible"

        mock_internet.return_value = True
        mock_valid_url.return_value = False
        assert (
            can_access_google_page("https://www.google.com") =="Not accessible"
        )

        mock_internet.return_value = False
        mock_valid_url.return_value = True
        assert (
            can_access_google_page("https://www.google.com") == "Not accessible"
        )
