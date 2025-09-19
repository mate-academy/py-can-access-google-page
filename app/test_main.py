from unittest import mock
from main import can_access_google_page


@mock.patch("main.valid_google_url")
@mock.patch("main.has_internet_connection")
def test_accessible_when_url_and_connection_are_true(
        mock_has_conn: mock.MagicMock,
        mock_valid_url: mock.MagicMock
) -> None:
    mock_has_conn.return_value = True
    mock_valid_url.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("main.valid_google_url")
@mock.patch("main.has_internet_connection")
def test_not_accessible_when_only_url_is_true(
        mock_has_conn: mock.MagicMock,
        mock_valid_url: mock.MagicMock
) -> None:
    mock_has_conn.return_value = False
    mock_valid_url.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("main.valid_google_url")
@mock.patch("main.has_internet_connection")
def test_not_accessible_when_only_connection_is_true(
        mock_has_conn: mock.MagicMock,
        mock_valid_url: mock.MagicMock
) -> None:
    mock_has_conn.return_value = True
    mock_valid_url.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("main.valid_google_url")
@mock.patch("main.has_internet_connection")
def test_not_accessible_when_both_are_false(
        mock_has_conn: mock.MagicMock,
        mock_valid_url: mock.MagicMock
) -> None:
    mock_has_conn.return_value = False
    mock_valid_url.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"
