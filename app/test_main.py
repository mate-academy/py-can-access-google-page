import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection, valid_google_url, expected_result",
    [
        pytest.param(False, False, "Not accessible",
                     id="has no connection, not correct url - Not accessible"),
        pytest.param(True, True, "Accessible",
                     id="has connection and correct url - Accessible"),
        pytest.param(True, False, "Not accessible",
                     id="has connection and not correct url - Not accessible"),
        pytest.param(False, True, "Not accessible",
                     id="has no connection and correct url - Not accessible"),
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: MagicMock,
        mock_valid_google_url: MagicMock,
        has_internet_connection: bool,
        valid_google_url: bool,
        expected_result: str
) -> None:
    mock_has_internet_connection.return_value = has_internet_connection
    mock_valid_google_url.return_value = valid_google_url

    assert can_access_google_page("google.com") == expected_result
