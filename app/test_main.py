import pytest
from unittest.mock import patch, MagicMock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection, valid_url, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Both valid and connected should be Accessible",
        "Invalid url should be Not accessible",
        "No internet should be Not accessible",
        "No internet and invalid url should be Not accessible"
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet_connection: MagicMock,
    mock_valid_google_url: MagicMock,
    internet_connection: bool,
    valid_url: bool,
    expected: str
) -> None:
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = valid_url

    assert can_access_google_page("https://www.google.com") == expected

    mock_has_internet_connection.assert_called_once()

    if internet_connection:
        mock_valid_google_url.assert_called_once_with("https://www.google.com")
    else:
        mock_valid_google_url.assert_not_called()
