from unittest import mock


from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
def test_has_been_has_internet_connection_called(
        m_has_internet_connection: object
) -> None:
    m_has_internet_connection.return_value = True
    can_access_google_page("https://www.google.com/")
    m_has_internet_connection.assert_called_once()


@mock.patch("app.main.valid_google_url")
def test_has_been_valid_google_url_called(m_valid_google_url: object) -> None:
    m_valid_google_url.return_value = True
    can_access_google_page("https://www.google.com/")
    m_valid_google_url.assert_called_once_with("https://www.google.com/")
