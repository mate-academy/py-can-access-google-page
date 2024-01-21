from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet: None,
                                mock_valid_google_url: None
                                ) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet.return_value = True
    assert can_access_google_page("http://example.com") == "Accessible"
    mock_valid_google_url.assert_called_with("http://example.com")
    mock_has_internet.assert_called_once()

    mock_valid_google_url.return_value = False
    mock_has_internet.return_value = False
    assert can_access_google_page("http://example.com") == "Not accessible"
    mock_valid_google_url.assert_called_with("http://example.com")
    mock_has_internet.assert_called()

    mock_valid_google_url.return_value = False
    mock_has_internet.return_value = True
    assert can_access_google_page("http://example.com") == "Not accessible"
    mock_valid_google_url.assert_called_with("http://example.com")
    mock_has_internet.assert_called()

    mock_valid_google_url.return_value = True
    mock_has_internet.return_value = False
    assert can_access_google_page("http://example.com") == "Not accessible"
    mock_valid_google_url.assert_called_with("http://example.com")
    mock_has_internet.assert_called()
