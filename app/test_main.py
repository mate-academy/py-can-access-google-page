import pytest
from unittest.mock import Mock, patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, has_connection, result",
    [
        pytest.param("https://mate.academy/", True, True, "Accessible", id="First"),
        pytest.param("https://google.com/", False, True, "Not accessible", id="Second"),
        pytest.param("https://googleboom.com/", True, False, "Not accessible", id="Third")
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_valid_url_and_connection_exists(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock,
        result: str,
        has_connection: bool,
        valid_url: bool,
        url: str
) -> None:
    mock_has_internet_connection.return_value = has_connection
    mock_valid_google_url.return_value = valid_url

    assert can_access_google_page(url) == result

    mock_has_internet_connection.assert_called_once()

    if has_connection:
        mock_valid_google_url.assert_called_once()
    else:
        mock_valid_google_url.assert_not_called()
