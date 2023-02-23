from app.main import can_access_google_page
from unittest import mock


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_true_true(
        mock_validate_google_url: mock,
        mock_has_internet_connection: mock
) -> None:
    mock_validate_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    url = "https://www.google.com/"
    assert can_access_google_page(url) == "Accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_true_false(
        mock_validate_google_url: mock,
        mock_has_internet_connection: mock
) -> None:
    mock_validate_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    url = "https://www.google.com/"
    assert can_access_google_page(url) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_false_true(
        mock_validate_google_url: mock,
        mock_has_internet_connection: mock
) -> None:
    mock_validate_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    url = "https://www.google.com/"
    assert can_access_google_page(url) == "Not accessible"


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_false_false(
        mock_validate_google_url: mock,
        mock_has_internet_connection: mock
) -> None:
    mock_validate_google_url.return_value = False
    mock_has_internet_connection.return_value = False
    url = "https://www.google.com/"
    assert can_access_google_page(url) == "Not accessible"
