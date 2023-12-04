from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    with mock.patch("app.main.has_internet_connection") as h_i_c, \
            mock.patch("app.main.valid_google_url") as v_g_u:
        h_i_c.return_value = True
        v_g_u.return_value = True

        assert can_access_google_page("http://google.com") == "Accessible"


def test_should_return_not_accessible_if_not_valid_google_url() -> None:
    with mock.patch("app.main.has_internet_connection") as h_i_c, \
            mock.patch("app.main.valid_google_url") as v_g_u:
        h_i_c.return_value = True
        v_g_u.return_value = False

        assert can_access_google_page("http://google.com") == "Not accessible"


def test_should_return_not_accessible_if_not_internet_connection() -> None:
    with mock.patch("app.main.has_internet_connection") as h_i_c, \
            mock.patch("app.main.valid_google_url") as v_g_u:
        h_i_c.return_value = False
        v_g_u.return_value = True

        assert can_access_google_page("http://google.com") == "Not accessible"
