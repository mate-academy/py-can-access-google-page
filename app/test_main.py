from unittest import mock

import pytest

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page(
        mock_internet: mock.MagicMock,
        mock_valid: mock.MagicMock
) -> None:
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_can_access_google_page_when_invalid_url(
        mock_internet: mock.MagicMock,
        mock_valid: mock.MagicMock
) -> None:
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_valid_google_url_is_called_with_url(
        mock_internet: mock.MagicMock,
        mock_valid: mock.MagicMock
) -> None:
    url = "http$://www.g00g1e.c0m"

    can_access_google_page(url)

    mock_valid.assert_called_once_with(url)


@pytest.mark.parametrize(
    "internet_available, expected",
    [
        (False, "Not accessible"),
        (True, "Accessible"),
    ],
)
@mock.patch("app.main.valid_google_url", return_value=True)
def test_can_access_google_page_with_internet(
        mock_valid: mock.MagicMock,
        internet_available: bool,
        expected: str
) -> None:
    # Мокаємо саму функцію has_internet_connection на потрібне значення
    with mock.patch(
            "app.main.has_internet_connection",
            return_value=internet_available
    ):
        result = can_access_google_page("https://www.google.com")
        assert result == expected
