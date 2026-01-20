import pytest
from unittest.mock import patch
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url_status,internet_status,expected_result",
    [
        pytest.param(
            True,
            True,
            "Accessible",
            id="two parameters are correct"
        ),
        pytest.param(
            False,
            True,
            "Not accessible",
            id="url status is False parameters are correct"
        ),
        pytest.param(
            True,
            False,
            "Not accessible",
            id="internet status is False parameters are correct"
        )
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_valid_url: bool,
    mock_internet_connection: bool,
    internet_status: bool,
    url_status: bool,
    expected_result: str
) -> None:
    mock_internet_connection.return_value = internet_status
    mock_valid_url.return_value = url_status
    result = can_access_google_page("https://example.com")
    assert result == expected_result
