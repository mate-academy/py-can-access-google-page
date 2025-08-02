from unittest import mock, TestCase

from app.main import can_access_google_page


class TestCanAccessGooglePage(TestCase):

    def setUp(self) -> None:
        self.mock_valid_url = mock.patch("app.main.valid_google_url").start()
        self.mock_internet = mock.patch(
            "app.main.has_internet_connection"
        ).start()

    def tearDown(self) -> None:
        mock.patch.stopall()

    def test_should_return_accessible_when_both_conditions_true(self) -> None:
        self.mock_valid_url.return_value = True
        self.mock_internet.return_value = True

        assert can_access_google_page("https://google.com") == "Accessible"

    def test_should_return_not_accessible_when_internet_false(self) -> None:
        self.mock_valid_url.return_value = True
        self.mock_internet.return_value = False

        assert can_access_google_page("https://google.com") == "Not accessible"

    def test_should_return_not_accessible_when_url_not_valid(self) -> None:
        self.mock_valid_url.return_value = False
        self.mock_internet.return_value = True

        assert can_access_google_page("https://google.com") == "Not accessible"

    def test_should_return_not_accessible_when_both_false(self) -> None:
        self.mock_valid_url.return_value = False
        self.mock_internet.return_value = False

        assert can_access_google_page("https://google.com") == "Not accessible"
