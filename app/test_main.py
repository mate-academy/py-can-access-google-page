import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,connection_exists,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet_connection: mock.MagicMock,
    mock_valid_google_url: mock.MagicMock,
    valid_url: bool,
    connection_exists: bool,
    expected: str
) -> None:
    mock_has_internet_connection.return_value = connection_exists
    mock_valid_google_url.return_value = valid_url
    assert can_access_google_page("https://google.com") == expected
