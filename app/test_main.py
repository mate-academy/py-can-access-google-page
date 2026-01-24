from unittest import mock


from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_has_internet, mock_google_url):
    test_cases = [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]

    for google_url, has_internet, expected in test_cases:
        mock_google_url.return_value = google_url
        mock_has_internet.return_value = has_internet
        result = can_access_google_page("https://google.com")

        assert result == expected

