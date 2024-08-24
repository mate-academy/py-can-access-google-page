from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page():
    with mock.patch(
            'main.valid_google_url',
            return_value=True
    ) as mock_valid_url,\
        mock.patch(
            'main.has_internet_connection',
            return_value=True
        ) as mock_internet:
        result = "http://google.com"
        assert result == "Not accessible"

    with mock.patch(
            'main.valid_google_url',
            return_value=False
                    ) as mock_valid_url, \
            mock.patch(
                'main.has_internet_connection',
                return_value=True
            ) as mock_internet:
        result = can_access_google_page("http://google.com")
        assert result == "Not accessible"

    with mock.patch(
            'main.valid_google_url',
            return_value=True
    ) as mock_valid_url, \
            mock.patch(
                'main.has_internet_connection',
                return_value=False
            ) as mock_internet:
        result = can_access_google_page("http://google.com")
        assert result == "Not accessible"
