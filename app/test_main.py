from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_called_function(mock_internet, mock_valid) -> None:
    page = "http://seasonvar.ru/serial-11941-Tajny_Broukenvuda.html"

    can_access_google_page(page)

    mock_internet.assert_called_once()
    mock_valid.assert_called_once_with(page)


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_accessible(mock_internet, mock_valid) -> None:
    page = "http://seasonvar.ru/serial-11941-Tajny_Broukenvuda.html"

    mock_internet.return_value = True
    mock_valid.return_value = True

    assert can_access_google_page(page) == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_internet_not_accessible(mock_internet, mock_valid) -> None:
    page = "http://seasonvar.ru/serial-11941-Tajny_Broukenvuda.html"

    mock_internet.return_value = False
    mock_valid.return_value = True

    assert can_access_google_page(page) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_google_url_not_accessible(mock_internet, mock_valid) -> None:
    page = "http://seasonvar.ru/serial-11941-Tajny_Broukenvuda.html"

    mock_internet.return_value = True
    mock_valid.return_value = False

    assert can_access_google_page(page) == "Not accessible"
