from unittest import mock

from app.main import can_access_google_page


def test_access_page():
    with mock.patch("app.main.valid_google_url")\
            as mocked_url_func:
        mocked_url_func.return_value = True

        with mock.patch("app.main.has_internet_connection")\
                as mocked_internet_func:
            mocked_internet_func.return_value = True

            assert can_access_google_page("url") == "Accessible"


def test_not_is_valid_url():
    with mock.patch("app.main.valid_google_url")\
            as mocked_url_func:
        mocked_url_func.return_value = False

        with mock.patch("app.main.has_internet_connection")\
                as mocked_internet_func:
            mocked_internet_func.return_value = True

            assert can_access_google_page("url") == "Not accessible"


def test_not_connection_internet():
    with mock.patch("app.main.valid_google_url")\
            as mocked_url_func:
        mocked_url_func.return_value = True

        with mock.patch("app.main.has_internet_connection")\
                as mocked_internet_func:
            mocked_internet_func.return_value = False

            assert can_access_google_page("url") == "Not accessible"
