import app.main
from app.main import can_access_google_page
from unittest import mock


def test_access_googl_page_without_internet() -> None:
    app.main.valid_google_url = mock.MagicMock(return_value=True)
    app.main.has_internet_connection = mock.MagicMock(return_value=False)
    assert can_access_google_page("https://translate.google.com/"
                                  "?sl=ru&tl=en&text=%D0%BA%D0"
                                  "%BE%D0%BD%D0%B2%D0%"
                                  "B5%D1%80%D1%82%D0%B0%D1%86%D0%B8%D1%8F&op"
                                  "=translate") == "Not accessible"


def test_access_googl_page_without_valid_url() -> None:
    app.main.valid_google_url = mock.MagicMock(return_value=False)
    app.main.has_internet_connection = mock.MagicMock(return_value=True)
    assert can_access_google_page("https://translate.google.com/"
                                  "?sl=ru&tl=en&text=%D0%BA%D0%"
                                  "BE%D0%BD%D0%B2%D0%"
                                  "B5%D1%80%D1%82%D0%B0%D1%86%D0%B8%D1%8F&op"
                                  "=translate") == "Not accessible"


def test_access_googl_page() -> None:
    app.main.valid_google_url = mock.MagicMock(return_value=True)
    app.main.has_internet_connection = mock.MagicMock(return_value=True)
    assert can_access_google_page("https://translate.google.com/"
                                  "?sl=ru&tl=en&text=%D0%BA%D0%BE%"
                                  "D0%BD%D0%B2%D0%"
                                  "B5%D1%80%D1%82%D0%B0%D1%86%D0%B8%D1%8F&op"
                                  "=translate") == "Accessible"
