from unittest.mock import patch, Mock
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_cannot_access_if_connection_or_valid_url_is_true(
    mock_valid_url: Mock, mock_internet: Mock
) -> None:
    # Перевірка, коли є інтернет, але URL неправильний
    mock_internet.return_value = True
    mock_valid_url.return_value = False
    result = can_access_google_page("https://www.fakegoogle.com")
    assert result == "Not accessible"

    # Перевірка, коли немає інтернету, але URL правильний
    mock_internet.return_value = False
    mock_valid_url.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_cannot_access_if_only_connection(
    mock_valid_url: Mock, mock_internet: Mock
) -> None:
    # Перевірка, коли є тільки інтернет, але URL неправильний
    mock_internet.return_value = True
    mock_valid_url.return_value = False
    result = can_access_google_page("https://www.fakegoogle.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_cannot_access_if_only_valid_url(
    mock_valid_url: Mock, mock_internet: Mock
) -> None:
    # Перевірка, коли правильний URL, але немає інтернету
    mock_internet.return_value = False
    mock_valid_url.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_accessible_when_both_true(
    mock_valid_url: Mock, mock_internet: Mock
) -> None:
    # Перевірка, коли є інтернет і правильний URL
    mock_internet.return_value = True
    mock_valid_url.return_value = True
    result = can_access_google_page("https://www.google.com")
    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_not_accessible_when_both_false(
    mock_valid_url: Mock, mock_internet: Mock
) -> None:
    # Перевірка, коли немає інтернету і неправильний URL
    mock_internet.return_value = False
    mock_valid_url.return_value = False
    result = can_access_google_page("https://www.fakegoogle.com")
    assert result == "Not accessible"
