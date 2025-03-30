from app.main import can_access_google_page
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "internet_connection, url, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_internet_connection: mock,
                                mock_url: mock,
                                internet_connection: bool,
                                url: bool,
                                result: str) -> None:
    mock_internet_connection.return_value = internet_connection
    mock_url.return_value = url
    assert can_access_google_page("") == result
