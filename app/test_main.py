import pytest
from unittest import mock
from app.main import can_access_google_page

@pytest.fixture(scope="module")
def get_url() -> str:
    return 'https://some-url.com'

class TestAccessGooglePage:
    @pytest.mark.parametrize(
        "mock_connection_value,mock_url_value,expected_access",
        [
            pytest.param(
                True,
                True,
                "Accessible",
                id="should have an access if has internet connection and valid google url"
            ),
            pytest.param(
                False,
                True,
                "Not accessible",
                id="should not have an access if no internet connection and valid google url"
            ),
            pytest.param(
                True,
                False,
                "Not accessible",
                id="should not have an access if has internet connection and not valid google url"
            ),
            pytest.param(
                False,
                False,
                "Not accessible",
                id="should not have an access if no internet connection and not valid google url"
            )
        ]
    )

    @mock.patch('app.main.has_internet_connection')
    @mock.patch('app.main.valid_google_url')
    def test_access_google_page(
            self,
            mock_valid_google_url,
            mock_has_internet_connection,
            get_url,
            mock_connection_value,
            mock_url_value,
            expected_access
    ):
        mock_has_internet_connection.return_value = mock_connection_value
        mock_valid_google_url.return_value = mock_url_value

        assert can_access_google_page(get_url) == expected_access
