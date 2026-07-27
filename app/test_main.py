import pytest
from unittest import mock
from unittest.mock import MagicMock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection,is_valid_url,input_url,expected_output",
    [
        (True, True, "https://www.google.com", "Accessible"),
        (False, True, "https://www.youtube.com", "Not accessible"),
        (True, False, "https://www.go000ogle.com", "Not accessible"),
        (False, False, "https://www.google.com", "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_accessible(
        mock_has_internet: MagicMock,
        mock_valid_url: MagicMock,
        has_connection: bool,
        is_valid_url: bool,
        input_url: str,
        expected_output: str
) -> None:
    mock_has_internet.return_value = has_connection
    mock_valid_url.return_value = is_valid_url
    assert can_access_google_page(input_url) == expected_output

    mock_has_internet.assert_called_once()

    if has_connection:
        mock_valid_url.assert_called_once_with(input_url)
    else:
        mock_valid_url.assert_not_called()
