from unittest import mock

from app.main import can_access_google_page


def test_can_access_google_page_accessible() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mocked_func1,
        mock.patch("app.main.valid_google_url") as mocked_func2
    ):
        mocked_func1.return_value = True
        mocked_func2.return_value = True
        assert can_access_google_page("") == "Accessible"


def test_can_access_google_page_not_accessible() -> None:
    with (
        mock.patch("app.main.has_internet_connection") as mocked_func1,
        mock.patch("app.main.valid_google_url") as mocked_func2
    ):
        mocked_func1.return_value = False
        mocked_func2.return_value = True
        assert can_access_google_page("") == "Not accessible"
        mocked_func1.return_value = True
        mocked_func2.return_value = False
        assert can_access_google_page("") == "Not accessible"
        mocked_func1.return_value = False
        mocked_func2.return_value = False
        assert can_access_google_page("") == "Not accessible"
