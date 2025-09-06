from app.main import can_access_google_page
from unittest.mock import patch


# Тест коли є інтернет і валідний url
def test_accessible_when_internet_and_valid_url() -> None:
    with patch("app.main.has_internet_connection",
               return_value=True) as mock_net, \
         patch("app.main.valid_google_url", return_value=True) as mock_url:
        url = "https://google.com"
        result = can_access_google_page(url)

        assert result == "Accessible"
        mock_net.assert_called_once_with()
        mock_url.assert_called_once_with(url)


# Тест коли є інтернет але не валідний url
def test_not_accessible_when_internet_true_but_invalid_url() -> None:
    with patch("app.main.has_internet_connection",
               return_value=True) as mock_net, \
         patch("app.main.valid_google_url", return_value=False) as mock_url:
        url = "https://not-google.com"
        result = can_access_google_page(url)

        assert result == "Not accessible"
        mock_net.assert_called_once_with()
        mock_url.assert_called_once_with(url)


# Тест коли не має інтернету (перевірка url не відбувається)
def test_not_accessible_when_no_internet_short_circuits_url_check() -> None:
    with patch("app.main.has_internet_connection",
               return_value=False) as mock_net, \
         patch("app.main.valid_google_url", return_value=True) as mock_url:
        url = "https://google.com"
        result = can_access_google_page(url)

        assert result == "Not accessible"
        mock_net.assert_called_once_with()
        mock_url.assert_not_called()
