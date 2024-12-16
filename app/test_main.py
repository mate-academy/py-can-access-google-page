from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_access_to_webpage(mock_has_internet_connection,
                           mock_valid_google_url):

    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    assert (can_access_google_page("https://www.google.com")
            == "Accessible")

    mock_has_internet_connection.return_value = False
    assert (can_access_google_page("https://www.google.com")
            == "Not accessible")

    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False
    assert (can_access_google_page("https://www.google.com")
            == "Not accessible")
