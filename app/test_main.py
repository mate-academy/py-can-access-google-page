import pytest
from unittest import mock
from app import main


@pytest.mark.parametrize(
    "url, expected",
    [
        ("https://www.google.com", "Accessible"),
    ],
)
def test_can_access_google_page(url, expected):
    with (
        mock.patch("app.main.valid_google_url") as mock_valid_url,
        mock.patch("app.main.has_internet_connection") as mock_internet_connection,
    ):
        mock_valid_url.return_value = True
        mock_internet_connection.return_value = True

        result = main.can_access_google_page(url)

        assert result == expected
        mock_internet_connection.assert_called_once()
        mock_valid_url.assert_called_once_with(url)
