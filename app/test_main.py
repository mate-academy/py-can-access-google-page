from app.main import can_access_google_page
from unittest import mock


def test_can_access_when_url_and_connection_are_valid() -> None:
    url = "https://google.com"
    with (
        mock.patch(
            "app.main.valid_google_url", return_value=True
        ) as valid_url_mock,
        mock.patch(
            "app.main.has_internet_connection", return_value=True
        ) as internet_mock
    ):
        result = can_access_google_page(url)
        assert result == "Accessible"
        valid_url_mock.assert_called_once_with(url)
        internet_mock.assert_called_once_with()


def test_cannot_access_when_no_connection() -> None:
    url = "https://google.com"
    with mock.patch(
        "app.main.has_internet_connection", return_value=False
    ) as internet_mock:
        result = can_access_google_page(url)
        assert result == "Not accessible"
        internet_mock.assert_called_once_with()


def test_cannot_access_when_invalid_url() -> None:
    url = "https://invalid-url.com"
    with (
        mock.patch(
            "app.main.valid_google_url", return_value=False
        ) as valid_url_mock,
        mock.patch(
            "app.main.has_internet_connection", return_value=True
        ) as internet_mock
    ):
        result = can_access_google_page(url)
        assert result == "Not accessible"
        valid_url_mock.assert_called_once_with(url)
        internet_mock.assert_called_once_with()


def test_cannot_access_when_no_connection_and_invalid_url() -> None:
    url = "https://invalid-url.com"
    with (
        mock.patch(
            "app.main.valid_google_url", return_value=False
        ) as valid_url_mock,
        mock.patch(
        "app.main.has_internet_connection", return_value=False
    ) as internet_mock
        ):
        result = can_access_google_page(url)
        assert result == "Not accessible"
        internet_mock.assert_called_once_with()
