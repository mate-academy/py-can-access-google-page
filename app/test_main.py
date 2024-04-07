from unittest import mock


from app.main import can_access_google_page


class TestAccessPage:
    def test_access_google_page_with_invalid_url(self) -> None:
        with mock.patch("app.main.valid_google_url")\
             as mock_valid_google_url,\
             mock.patch("app.main.has_internet_connection")\
             as mock_has_internet_connection:

            mock_valid_google_url.return_value = False
            mock_has_internet_connection.return_value = True
            assert can_access_google_page("https://example.com") ==\
                   "Not accessible"

    def test_access_google_page_without_internet(self) -> None:
        with mock.patch("app.main.valid_google_url")\
             as mock_valid_google_url,\
             mock.patch("app.main.has_internet_connection")\
             as mock_has_internet_connection:

            mock_valid_google_url.return_value = True
            mock_has_internet_connection.return_value = False
            assert can_access_google_page("https://www.google.com") ==\
                   "Not accessible"

    def test_access_google_page_with_url_and_internet(self) -> None:
        with mock.patch("app.main.valid_google_url")\
             as mock_valid_google_url,\
             mock.patch("app.main.has_internet_connection")\
             as mock_has_internet_connection:

            mock_valid_google_url.return_value = True
            mock_has_internet_connection.return_value = True
            assert can_access_google_page("https://www.google.com") ==\
                   "Accessible"
