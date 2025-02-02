import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url() -> mock.Mock:
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mock_has_internet_connection() -> mock.Mock:
    with mock.patch("app.main.has_internet_connection") as mock_internet:
        yield mock_internet


@pytest.mark.parametrize(
    "mock_url, mock_internet, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(
        mock_valid_google_url: mock.Mock,
        mock_has_internet_connection: mock.Mock,
        mock_url: bool,
        mock_internet: bool,
        expected: str
        ) -> None:
    mock_valid_google_url.return_value = mock_url
    mock_has_internet_connection.return_value = mock_internet
    result = can_access_google_page("https://www.google.com")
    assert result == expected
