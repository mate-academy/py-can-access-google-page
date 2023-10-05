import pytest
from unittest.mock import Mock, patch


from app.main import can_access_google_page


@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "valid_url, has_internet, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
)
def test_can_access_google_page(
        mock_valid_google_url: Mock,
        mock_has_internet_connection: Mock,
        valid_url: bool,
        has_internet: bool,
        expected_result: str
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = has_internet

    assert can_access_google_page(valid_url) == expected_result
