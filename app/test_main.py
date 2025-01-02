from unittest import mock


from app.main import can_access_google_page


def test_functions_are_called() -> None:
    with mock.patch("app.main.has_internet_connection") as mock_i_con:
        can_access_google_page("http://google.com")
        mock_i_con.assert_called_once()

    with mock.patch("app.main.valid_google_url") as mock_v_url:
        can_access_google_page("http://google.com")
        mock_v_url.assert_called_once_with("http://google.com")
