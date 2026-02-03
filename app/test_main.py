from unittest import mock
from unittest.mock import Mock

from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with (mock.patch("app.main.valid_google_url") as mock_valid_google_url,
          mock.patch("app.main.has_internet_connection") as mock_has_internet):
        mock_valid_google_url.return_value = True
        mock_has_internet.return_value = True

        assert can_access_google_page(
            "https://www.google.com") == "Accessible"
        mock_valid_google_url.assert_called_once_with("https://www.google.com")
        mock_has_internet.assert_called_once()


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_not_access_google_page(
        mock_has_internet: Mock,
        mock_valid_url: Mock
) -> None:
    mock_valid_url.return_value = False
    mock_has_internet.return_value = True

    assert can_access_google_page("https://www.google.com") == "Not accessible"
    mock_valid_url.assert_called_once_with("https://www.google.com")
    mock_has_internet.assert_called_once()
