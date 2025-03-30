from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection, valid_google_url, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
# @mock.patch("app.main.has_internet_connection")
# @mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
    has_internet_connection: bool,
    valid_google_url: bool,
    expected_result: str
) -> None:
    with (mock.patch("app.main.has_internet_connection")
          as mock_has_internet_connection,
          mock.patch("app.main.valid_google_url")
          as mock_valid_google_url):
        mock_has_internet_connection.return_value = has_internet_connection
        mock_valid_google_url.return_value = valid_google_url
        assert (can_access_google_page(str(mock_valid_google_url))
                == expected_result)
