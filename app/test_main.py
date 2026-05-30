from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet: mock.MagicMock,
        mock_valid_google_url: mock.MagicMock,
) -> None:
    mock_has_internet.return_value = True
    mock_valid_google_url.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"
