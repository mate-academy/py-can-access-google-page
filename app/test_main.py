from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_accessible(
    mock_valid_url: mock.MagicMock,
    mock_connection: mock.MagicMock
) -> None:
    """Перевірка повного доступу: і інтернет, і URL валідні"""
    mock_valid_url.return_value = True
    mock_connection.return_value = True

    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_cannot_access_if_only_connection_is_true(
    mock_valid_url: mock.MagicMock,
    mock_connection: mock.MagicMock
) -> None:
    """Перевірка: інтернет є, але URL невалідний -> Not accessible"""
    mock_valid_url.return_value = False
    mock_connection.return_value = True

    assert can_access_google_page("https://invalid.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_cannot_access_if_only_valid_url_is_true(
    mock_valid_url: mock.MagicMock,
    mock_connection: mock.MagicMock
) -> None:
    """Перевірка: URL валідний, але інтернету немає -> Not accessible"""
    mock_valid_url.return_value = True
    mock_connection.return_value = False

    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_cannot_access_if_both_are_false(
    mock_valid_url: mock.MagicMock,
    mock_connection: mock.MagicMock
) -> None:
    """Перевірка: ні інтернету, ні валідного URL -> Not accessible"""
    mock_valid_url.return_value = False
    mock_connection.return_value = False

    assert can_access_google_page("https://invalid.com") == "Not accessible"
