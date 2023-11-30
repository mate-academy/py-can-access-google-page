import pytest
from unittest import mock

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.fixture()
    def url(self) -> str:
        return "https://www.google.com"

    @mock.patch("app.main.valid_google_url", return_value=False)
    def test_if_not_valid_google_url(
        self,
        mocked_valid_google_url_false: mock.MagicMock,
        url: str
    ) -> None:
        assert can_access_google_page(url) == "Not accessible"

    @mock.patch("app.main.has_internet_connection", return_value=False)
    def test_if_has_not_internet_connection(
        self,
        mocked_has_internet_connection_false: mock.MagicMock,
        url: str
    ) -> None:
        assert can_access_google_page(url) == "Not accessible"

    @mock.patch("app.main.has_internet_connection", return_value=False)
    @mock.patch("app.main.valid_google_url", return_value=False)
    def test_if_all_is_false(
        self,
        mocked_valid_google_url_false: mock.MagicMock,
        mocked_has_internet_connection_false: mock.MagicMock,
        url: str
    ) -> None:
        assert can_access_google_page(url) == "Not accessible"

    @mock.patch("app.main.has_internet_connection", return_value=True)
    @mock.patch("app.main.valid_google_url", return_value=True)
    def test_if_all_is_true(
        self,
        mocked_valid_google_url_true: mock.MagicMock,
        mocked_has_internet_connection_true: mock.MagicMock,
        url: str
    ) -> None:
        assert can_access_google_page(url) == "Accessible"
