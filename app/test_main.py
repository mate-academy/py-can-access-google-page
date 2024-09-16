from unittest import mock
import pytest

from app.main import can_access_google_page


class TestCanAccessGooglePage:
    @pytest.fixture()
    def mocked_valid_google_url(self):
        with mock.patch("app.main.valid_google_url") as \
                mocked_valid_google_url:
            yield mocked_valid_google_url

    @pytest.fixture()
    def mocked_has_internet_connection(self):
        with mock.patch("app.main.has_internet_connection") as \
                mocked_has_internet_connection:
            yield mocked_has_internet_connection

    @pytest.mark.parametrize(
        "valid_google_url,has_internet_connection,initial_url,expected_value",
        [
            (True, True, "google.com", "Accessible"),
            (False, True, "google.com", "Not accessible"),
            (True, False, "google.com", "Not accessible"),
            (False, False, "google.com", "Not accessible"),
        ]
    )
    def test_can_access_google_page(
            self,
            valid_google_url,
            has_internet_connection,
            initial_url,
            expected_value,
            mocked_valid_google_url,
            mocked_has_internet_connection):
        mocked_valid_google_url.return_value = valid_google_url
        mocked_has_internet_connection.return_value = has_internet_connection

        assert can_access_google_page(initial_url) == expected_value
