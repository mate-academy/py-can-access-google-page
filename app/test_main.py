from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(mock_internet_connection: bool,
                                mock_valid_url: bool) -> None:
    mock_internet_connection.return_value = True
    mock_valid_url.return_value = True
    expected_output = "Accessible"
    assert can_access_google_page("http://www.google.com") == expected_output


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_not_valid_page(mock_internet_connection: bool,
                        mock_valid_url: bool) -> None:
    mock_internet_connection.return_value = True
    mock_valid_url.return_value = False
    expected_output = "Not accessible"
    assert can_access_google_page("http://invalid.url") == expected_output


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_no_internet(mock_internet_connection: bool,
                     mock_valid_url: bool) -> None:
    mock_internet_connection.return_value = False
    mock_valid_url.return_value = True
    expected_output = "Not accessible"
    assert can_access_google_page("http://www.google.com") == expected_output


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_both_false(mock_internet_connection: bool,
                    mock_valid_url: bool) -> None:
    mock_internet_connection.return_value = False
    mock_valid_url.return_value = False
    expected_output = "Not accessible"
    assert can_access_google_page("") == expected_output
