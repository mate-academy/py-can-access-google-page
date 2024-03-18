from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet_connection: mock,
                                mock_valid_google_url: mock) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True

    assert can_access_google_page("www.google.com") == "Accessible"

    mock_valid_google_url.return_value = False
    assert can_access_google_page("/www.invalidurl.com") == "Not accessible"

    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True
    assert can_access_google_page("www.google.com") == "Not accessible"

    mock_valid_google_url.return_value = False
    assert can_access_google_page("www.invalidurl.com") == "Not accessible"
