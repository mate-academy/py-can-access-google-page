from unittest import mock

from app.main import can_access_google_page


def test_access_if_has_internet_and_valid_url() -> None:
    with mock.patch(
            "app.main.has_internet_connection",
            return_value=True
    ) as mock_net, \
            mock.patch(
                "app.main.valid_google_url",
                return_value=True
    ) as mock_url:

        url = "https://google.com"
        result = can_access_google_page(url)

        assert result == "Accessible"

        mock_net.assert_called_once()
        mock_url.assert_called_once()


def test_access_if_has_internet_but_not_valid_url() -> None:
    with mock.patch(
            "app.main.has_internet_connection",
            return_value=True
    ) as mock_net, \
            mock.patch(
                "app.main.valid_google_url",
                return_value=False
    ) as mock_url:

        url = "https://google.com/invalid"
        result = can_access_google_page(url)

        assert result == "Not accessible"

        mock_net.assert_called_once()
        mock_url.assert_called_once()


def test_access_if_not_has_internet_but_valid_url() -> None:
    with mock.patch(
            "app.main.has_internet_connection",
            return_value=False
    ) as mock_net, \
            mock.patch(
                "app.main.valid_google_url",
                return_value=True
    ) as mock_url:

        url = "https://google.com"
        result = can_access_google_page(url)

        assert result == "Not accessible"

        mock_net.assert_called_once()
        mock_url.assert_not_called()
