from unittest import mock
import pytest
from app.main import can_access_google_page


class TestMain:
    @pytest.fixture
    def mock_valid_google_url(self):
        with mock.patch('app.main.valid_google_url') as mocked_google_url:
            yield mocked_google_url

    @pytest.fixture
    def mock_has_internet_connection(self):
        with mock.patch('app.main.has_internet_connection') as mocked_internet:
            yield mocked_internet

    @pytest.mark.parametrize(
        "valid_url, internet_connection, func_feedback",
        [
            pytest.param(
                True, False, "Not accessible",
                id="url is not valid"
            ),
            pytest.param(
                False, True, "Not accessible",
                id="no connection to internet"
            ),
            pytest.param(
                False, False, "Not accessible",
                id="url is not valid and "
                "no connection to internet"
            ),
            pytest.param(
                True, True, "Accessible",
                id="you can access to the site"
            )
        ]
    )
    def test_can_access_google_page(self,
                                    valid_url,
                                    internet_connection,
                                    func_feedback,
                                    mock_valid_google_url,
                                    mock_has_internet_connection):

        mock_valid_google_url.return_value = valid_url
        mock_has_internet_connection.return_value = internet_connection

        assert can_access_google_page("google.com") == func_feedback
