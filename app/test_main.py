import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture()
def mock_valid_google_url():
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mock_has_internet_connection():
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
def test_can_access_google_page(mock_valid_google_url,
                            mock_has_internet_connection,
                            mock_url_return: bool,
                            mock_connection_return: bool,
                            expected: str
                            ) -> None:
    mock_valid_google_url.return_value = mock_url_return
    mock_has_internet_connection.return_value = mock_connection_return
    result = can_access_google_page("https://www.google.com")
    assert result == expected
