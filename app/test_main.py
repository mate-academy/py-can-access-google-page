from unittest import mock
from unittest.mock import Mock

from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with (mock.patch("app.main.valid_google_url") as mock_valid_url,
          mock.patch("app.main.has_internet_connection") as mock_has_internet):
        mock_has_internet.return_value = True
        mock_valid_url.return_value = True

        assert can_access_google_page(
            "https://www.google.com") == "Accessible"
        mock_has_internet.assert_called_once()
        mock_valid_url.assert_called_once_with("https://www.google.com")


def test_can_not_access_google_page_when_no_internet() -> None:
    with (mock.patch("app.main.valid_google_url") as mock_valid_url,
          mock.patch("app.main.has_internet_connection") as mock_has_internet):
        mock_has_internet.return_value = False
        mock_valid_url.return_value = True

        assert can_access_google_page(
            "https://www.google.com") == "Not accessible"
        mock_has_internet.assert_called_once()
        mock_valid_url.assert_not_called()


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_not_access_google_page_when_invalid_url(
        mock_has_internet: Mock,
        mock_valid_url: Mock
) -> None:
    mock_has_internet.return_value = True
    mock_valid_url.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"
    mock_has_internet.assert_called_once()
    mock_valid_url.assert_called_once_with("https://www.google.com")


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_not_access_google_page_when_no_internet_and_invalid_url(
        mock_has_internet: Mock,
        mock_valid_url: Mock
) -> None:
    mock_has_internet.return_value = False
    mock_valid_url.return_value = False

    assert can_access_google_page("https://www.google.com") == "Not accessible"
    mock_has_internet.assert_called_once()
    mock_valid_url.assert_not_called()
