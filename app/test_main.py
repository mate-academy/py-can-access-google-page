from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_returns_accessible_when_url_is_valid_and_connection_exists(
        mock_connection: mock.MagicMock,
        mock_valid: mock.MagicMock
) -> None:
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.valid_google_url", return_value=False)
@mock.patch("app.main.has_internet_connection", return_value=True)
def test_returns_not_accessible_when_url_is_not_valid_and_connection_exists(
        mock_connection: mock.MagicMock,
        mock_valid: mock.MagicMock
) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url", return_value=True)
@mock.patch("app.main.has_internet_connection", return_value=False)
def test_returns_not_accessible_when_url_is_valid_and_connection_not_exists(
        mock_connection: mock.MagicMock,
        mock_valid: mock.MagicMock
) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"
