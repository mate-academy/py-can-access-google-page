from app.main import can_access_google_page
from unittest.mock import patch


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_if_condition_is_true_true(mock_url: str,
                                   mock_internet: str) -> bool:

    mock_url.return_value = True
    mock_internet.return_value = True

    result = can_access_google_page("url")
    assert result == "Accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_if_condition_is_true_false(mock_url: str,
                                    mock_internet: str) -> bool:

    mock_url.return_value = True
    mock_internet.return_value = False

    result = can_access_google_page("url")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_if_condition_is_false_true(mock_url: str,
                                    mock_internet: str) -> bool:

    mock_url.return_value = False
    mock_internet.return_value = True

    result = can_access_google_page("url")
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_if_condition_is_false_false(mock_url: str,
                                     mock_internet: str) -> bool:

    mock_url.return_value = False
    mock_internet.return_value = False

    result = can_access_google_page("url")
    assert result == "Not accessible"
