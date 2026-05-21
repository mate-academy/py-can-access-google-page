from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_accessible_when_both_true(
    mock_internet: mock.MagicMock,
    mock_url: mock.MagicMock,
) -> None:
    mock_internet.return_value = True
    mock_url.return_value = True
    assert can_access_google_page("https://google.com") == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_no_internet(
    mock_internet: mock.MagicMock,
    mock_url: mock.MagicMock,
) -> None:
    mock_internet.return_value = False
    mock_url.return_value = True
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_invalid_url(
    mock_internet: mock.MagicMock,
    mock_url: mock.MagicMock,
) -> None:
    mock_internet.return_value = True
    mock_url.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_accessible_when_both_false(
    mock_internet: mock.MagicMock,
    mock_url: mock.MagicMock,
) -> None:
    mock_internet.return_value = False
    mock_url.return_value = False
    assert can_access_google_page("https://google.com") == "Not accessible"
