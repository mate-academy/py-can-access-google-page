from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_for_access_to_page(mock_has_internet_connection: mock.MagicMock,
                            mock_valid_google_url: mock.MagicMock) -> None:
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
