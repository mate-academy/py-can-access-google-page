from unittest import mock
from unittest.mock import MagicMock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_google: MagicMock,
                                mock_has_internet: MagicMock) -> None:
    can_access_google_page("https://finance.yahoo.com/")
    mock_valid_google.assert_called_with("https://finance.yahoo.com/")
    mock_has_internet.assert_called()
