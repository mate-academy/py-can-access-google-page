import app.main
import pytest

from unittest import mock


@pytest.mark.parametrize(
"valid_url, has_internet, expected",
[(True, True, "Accessible"),
 (False, True, "Not accessible"),
 (True, False, "Not accessible"),
 (False, False, "Not accessible"),
 ])

@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_has_internet_connection: mock.MagicMock,
    mock_valid_google_url: mock.MagicMock,
    valid_url: bool,
    has_internet: bool,
    expected: str
) -> None:

    mock_has_internet_connection.return_value = has_internet
    mock_valid_google_url.return_value = valid_url

    result = app.main.can_access_google_page("https://www.google.com")
    assert result == expected
    mock_has_internet_connection.assert_called_once()
    mock_valid_google_url.assert_called_once_with("https://www.google.com")
