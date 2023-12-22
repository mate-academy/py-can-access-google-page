from unittest.mock import patch, Mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet, valid_url, expected_result",
    [
        pytest.param(False, True, "Not accessible",
                     id="URL valid but no connection"),
        pytest.param(True, False,
                     "Not accessible", id="URL invalid but connection exists"),
        pytest.param(False, False,
                     "Not accessible", id="URL invalid and no connection"),
        pytest.param(True, True,
                     "Accessible", id="URL valid and connection exists")
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_has_internet_connection: Mock,
    mock_valid_google_url: Mock,
    has_internet: bool,
    valid_url: bool,
    expected_result: str
) -> None:
    url = "https://www.google.com"
    mock_has_internet_connection.return_value = has_internet
    mock_valid_google_url.return_value = valid_url
    assert can_access_google_page(url) == expected_result
