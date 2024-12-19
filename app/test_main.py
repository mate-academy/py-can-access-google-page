import pytest
from unittest import mock
from app.main import can_access_google_page


def test_can_access_google_page() -> None:
    with (mock.patch("app.main.valid_google_url") as mock_valid_google_url,
            mock.patch("app.main.has_internet_connection")
            as mock_has_internet_connection):

        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = True
        assert can_access_google_page("https://google.com") == "Accessible"

        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = True
        assert can_access_google_page("https://google.com") == "Not accessible"

        mock_valid_google_url.return_value = True
        mock_has_internet_connection.return_value = False
        assert can_access_google_page("https://google.com") == "Not accessible"

        mock_valid_google_url.return_value = False
        mock_has_internet_connection.return_value = False
        assert can_access_google_page("https://google.com") == "Not accessible"


if __name__ == "__name__":
    pytest.main()
