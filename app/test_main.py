from unittest import mock
from app.main import can_access_google_page


def test_called_function() -> None:
    with (mock.patch("app.main.valid_google_url") as mock_valid,
          mock.patch("app.main.has_internet_connection") as mock_internet):
        page = "http://seasonvar.ru/serial-11941-Tajny_Broukenvuda.html"

        can_access_google_page(page)

        mock_internet.assert_called_once()
        mock_valid.assert_called_once_with(page)


def test_accessible() -> None:
    page = "http://seasonvar.ru/serial-11941-Tajny_Broukenvuda.html"
    with (mock.patch("app.main.valid_google_url") as mock_valid,
          mock.patch("app.main.has_internet_connection") as mock_internet):

        mock_internet.return_value = True
        mock_valid.return_value = True

        assert can_access_google_page(page) == "Accessible"
