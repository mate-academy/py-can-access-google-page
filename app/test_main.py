import pytest

from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, internet_connection, result",
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
        mock_valid_url: mock.MagicMock,
        mock_internet_connection: mock.MagicMock,
        valid_url: bool,
        internet_connection: bool,
        result: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_internet_connection.return_value = internet_connection
    assert can_access_google_page("https://mate.academy/") == result
