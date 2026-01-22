from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid: MagicMock,
        mock_inet: MagicMock
) -> None:
    mock_valid.return_value = False
    mock_inet.return_value = False
    assert (can_access_google_page("https://www.google.com/")
            == "Not accessible")
    mock_valid.return_value = True
    mock_inet.return_value = False
    assert (can_access_google_page("https://www.google.com/")
            == "Not accessible")
    mock_valid.return_value = False
    mock_inet.return_value = True
    assert (can_access_google_page("https://www.google.com/")
            == "Not accessible")
    mock_valid.return_value = True
    mock_inet.return_value = True
    assert (can_access_google_page("https://www.google.com/")
            == "Accessible")
