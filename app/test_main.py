from app.main import can_access_google_page
import pytest
from unittest import mock


url = "https://www.google.com"


@pytest.mark.parametrize(
    "valid_url,connection,expected_value",
    [(True, True, "Accessible"),
     (False, True, "Not accessible"),
     (True, False, "Not accessible"),
     (False, False, "Not accessible")]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_request(
        mock_valid_google_url: mock,
        mock_has_internet_connection: mock,
        expected_value: str,
        valid_url: bool,
        connection: bool
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = connection

    assert can_access_google_page(url) == expected_value
