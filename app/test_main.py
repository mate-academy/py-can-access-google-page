import pytest
from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@pytest.fixture
def mocked_has_internet_connection() -> MagicMock:
    with patch(
            "app.main.has_internet_connection"
    ) as mocked_has_internet_connection:
        yield mocked_has_internet_connection


@pytest.fixture
def mocked_valid_google_url() -> MagicMock:
    with patch("app.main.valid_google_url") as mocked_valid_google_url:
        yield mocked_valid_google_url


@pytest.mark.parametrize(
    "mock_has_inet_connect,mock_valid_url,expected_result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="Accessible when has internet connection and url is valid"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="Not accessible when invalid url"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="Not accessible when no internet connection"
        ),
    ]
)
def test_can_access_google_page(
        mock_has_inet_connect: bool,
        mock_valid_url: bool,
        expected_result: str,
        mocked_has_internet_connection: MagicMock,
        mocked_valid_google_url: MagicMock
) -> None:
    mocked_has_internet_connection.return_value = mock_has_inet_connect
    mocked_valid_google_url.return_value = mock_valid_url
    result = can_access_google_page("url")
    assert result == expected_result
