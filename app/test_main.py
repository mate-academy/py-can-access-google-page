from app.main import can_access_google_page
import pytest
from unittest import mock


@pytest.fixture()
def mock_valid_google_url():
    with mock.patch("app.main.valid_google_url") as mock_url:
        yield mock_url


@pytest.fixture()
def mock_internet_connection():
    with mock.patch("app.main.has_internet_connection") as mock_connection:
        yield mock_connection


class TestAccessGoogle:
    @pytest.mark.parametrize(
        "valid_google_url,internet_connection,result",
        [
            pytest.param(True, True, "Accessible",
                         id="1"),
            pytest.param(False, True, "Not accessible",
                         id="2"),
            pytest.param(True, False, "Not accessible",
                         id="3"),
            pytest.param(False, False, "Not accessible",
                         id="4")
        ]
    )
    def test_access_google_page(
            self,
            valid_google_url,
            internet_connection,
            result,
            mock_internet_connection,
            mock_valid_google_url
    ):
        mock_valid_google_url.return_value = valid_google_url
        mock_internet_connection.return_value = internet_connection
        assert can_access_google_page("") == result
