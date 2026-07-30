from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exist(mock_has_internet: MagicMock,
                                        mock_valid_url: MagicMock
                                        ) -> None:
    mock_has_internet.return_value = True
    mock_valid_url.return_value = True

    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"

    mock_has_internet.assert_called_once()
    mock_valid_url.assert_called_once_with("https://www.google.com")


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_valid_url_and_no_connection(mock_has_internet: MagicMock,
                                     mock_valid_url: MagicMock
                                     ) -> None:
    mock_has_internet.return_value = False
    mock_valid_url.return_value = True

    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"

    mock_has_internet.assert_called_once()


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_invalid_url_and_connection_exist(mock_has_internet: MagicMock,
                                          mock_valid_url: MagicMock
                                          ) -> None:
    mock_has_internet.return_value = True
    mock_valid_url.return_value = False

    result = can_access_google_page("htt://www.google.com")
    assert result == "Not accessible"

    mock_has_internet.assert_called_once()
    mock_valid_url.assert_called_once_with("htt://www.google.com")
