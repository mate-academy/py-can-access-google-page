from unittest import TestCase, mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
class TestCanAccessGooglePage(TestCase):
    def setUp(self) -> None:
        self.url = ""

    def test_no_internet(self,
                         mocked_url: bool,
                         mocked_internet: bool) -> None:
        mocked_internet.return_value = False
        mocked_url.return_value = True
        assert can_access_google_page(self.url) == "Not accessible", \
            "You don't have internet"

    def test_not_valid_url(self,
                           mocked_url: bool,
                           mocked_internet: bool) -> None:
        mocked_internet.return_value = True
        mocked_url.return_value = False
        assert can_access_google_page(self.url) == "Not accessible", \
            "Invalid url"

    def test_no_internet_not_valid_url(self,
                                       mocked_url: bool,
                                       mocked_internet: bool) -> None:
        mocked_internet.return_value = False
        mocked_url.return_value = False
        assert can_access_google_page(self.url) == "Not accessible", \
            "You don't have internet, invalid url"

    def test_internet_valid_url(self,
                                mocked_url: bool,
                                mocked_internet: bool) -> None:
        mocked_internet.return_value = True
        mocked_url.return_value = True
        assert can_access_google_page(self.url) == "Accessible", \
            "You have internet connection and url is valid " \
            "you should be able access google page"
