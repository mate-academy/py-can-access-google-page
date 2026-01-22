from unittest import mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,internet,is_valid",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: mock.MagicMock,
        mock_has_internet_connection: mock.MagicMock,
        url: bool,
        internet: bool,
        is_valid: str
) -> None:
    mock_valid_google_url.return_value = url
    mock_has_internet_connection.return_value = internet
    assert can_access_google_page("Google.com") == is_valid
