from unittest import mock
from unittest.mock import MagicMock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection,valid_url,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_to_google_page(
        mock_valid_url: MagicMock,
        mock_internet_connection: MagicMock,
        internet_connection: bool,
        valid_url: bool,
        result: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_internet_connection.return_value = internet_connection

    assert can_access_google_page(valid_url) == result
