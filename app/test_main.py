import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_connection, mock_valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_connection: bool,
        mocked_valid_url: bool,
        mock_connection: bool,
        mock_valid_url: bool,
        expected: str
) -> None:
    mocked_connection.return_value = mock_connection
    mocked_valid_url.return_value = mock_valid_url
    assert can_access_google_page("https://google.com") == expected
