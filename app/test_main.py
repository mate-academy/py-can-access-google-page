from unittest.mock import patch
from app.main import can_access_google_page


def test_accessible_when_url_valid_and_has_internet() -> None:
    with (patch("app.main.valid_google_url", return_value=True)
          as mocked_valid_url,
            patch("app.main.has_internet_connection", return_value=True)
            as mocked_internet_conn):
        result = can_access_google_page("https://google.com")
        assert result == "Accessible"
        mocked_valid_url.assert_called_once_with("https://google.com")
        mocked_internet_conn.assert_called_once()


def test_not_accessible_when_url_not_valid_and_has_internet() -> None:
    with (patch("app.main.valid_google_url", return_value=False)
          as mocked_valid_url,
            patch("app.main.has_internet_connection", return_value=True)
            as mocked_internet_conn):
        result = can_access_google_page("$&@^$^^&@#$%!*^")
        assert result == "Not accessible"
        mocked_valid_url.assert_called_once_with("$&@^$^^&@#$%!*^")
        mocked_internet_conn.assert_called_once()


def test_not_accessible_when_url_valid_and_has_not_internet() -> None:
    with (patch("app.main.valid_google_url", return_value=True)
          as mocked_valid_url,
            patch("app.main.has_internet_connection", return_value=False)
            as mocked_internet_conn):
        result = can_access_google_page("https://google.com")
        assert result == "Not accessible"
        mocked_internet_conn.assert_called_once()
        mocked_valid_url.assert_not_called()


def test_not_accessible_when_url_not_valid_and_has_not_internet() -> None:
    with (patch("app.main.valid_google_url", return_value=False)
          as mocked_valid_url,
            patch("app.main.has_internet_connection", return_value=False)
            as mocked_internet_conn):
        result = can_access_google_page("$&@^$^^&@#$%!*^")
        assert result == "Not accessible"
        mocked_internet_conn.assert_called_once()
        mocked_valid_url.assert_not_called()
