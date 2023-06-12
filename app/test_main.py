from app.main import can_access_google_page
from unittest import mock
import pytest


class TestCanAccessGooglePage:

    @pytest.fixture
    def mocked_valid_google_url(self) -> None:
        with (
            mock.patch("app.main.valid_google_url")
            as mocked_valid
        ):
            yield mocked_valid

    @pytest.fixture
    def mocked_has_internet_connection(self) -> None:
        with (
            mock.patch("app.main.has_internet_connection")
            as mocked_connection
        ):
            yield mocked_connection

    def test_valid_url_and_connection_exists(
            self,
            mocked_valid_google_url: mock.MagicMock,
            mocked_has_internet_connection: mock.MagicMock
    ) -> None:
        mocked_valid_google_url.return_value = True
        mocked_has_internet_connection.return_value = True

        result = can_access_google_page(
            "https://mate.academy/learn?course=all_courses"
        )

        assert result == "Accessible"

        mocked_valid_google_url.return_value = False
        mocked_has_internet_connection.return_value = True

        result = can_access_google_page(
            "https://mate.academy/learn?course=all_courses"
        )

        assert result == "Not accessible"

        mocked_valid_google_url.return_value = True
        mocked_has_internet_connection.return_value = False

        result = can_access_google_page(
            "https://mate.academy/learn?course=all_courses"
        )

        assert result == "Not accessible"

        mocked_valid_google_url.return_value = False
        mocked_has_internet_connection.return_value = False

        result = can_access_google_page(
            "https://mate.academy/learn?course=all_courses"
        )

        assert result == "Not accessible"
