import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.fixture
def get_valid_google_url() -> mock.MagicMock:
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture
def get_connection() -> mock.MagicMock:
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


@pytest.mark.parametrize(
    "valid_url, connection_status, expected_result",
    [
        pytest.param(True, True,
                     "Accessible",
                     id="access google page True"),
        pytest.param(True, False,
                     "Not accessible",
                     id="connection status False"),
        pytest.param(False, True,
                     "Not accessible",
                     id="valid url False"),
    ]
)
def test_1(get_valid_google_url: object,
           get_connection: object,
           valid_url: bool,
           connection_status: bool,
           expected_result: str) -> None:
    get_valid_google_url.return_value = valid_url
    get_connection.return_value = connection_status
    assert can_access_google_page("https://www.google.com") == expected_result
