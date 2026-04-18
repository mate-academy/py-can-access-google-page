from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_url: mock.MagicMock,
    mock_internet: mock.MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = True
    assert can_access_google_page("https://www.google.com") == "Accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_cannot_access_if_invalid_url(
    mock_valid_url: mock.MagicMock,
    mock_internet: mock.MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = True
    assert can_access_google_page("https://invalid.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_cannot_access_if_no_internet(
    mock_valid_url: mock.MagicMock,
    mock_internet: mock.MagicMock
) -> None:
    mock_valid_url.return_value = True
    mock_internet.return_value = False
    assert can_access_google_page("https://www.google.com") == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_cannot_access_if_both_conditions_false(
    mock_valid_url: mock.MagicMock,
    mock_internet: mock.MagicMock
) -> None:
    mock_valid_url.return_value = False
    mock_internet.return_value = False
    assert can_access_google_page("https://invalid.com") == "Not accessible"
