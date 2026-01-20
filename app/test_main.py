import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "first_initial_value,second_initial_value,expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
        (False, True, "Not accessible")
    ]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet: MagicMock,
        mock_valid_url: MagicMock,
        first_initial_value: bool,
        second_initial_value: bool,
        expected_result: str
) -> None:
    mock_has_internet.return_value = first_initial_value
    mock_valid_url.return_value = second_initial_value
    assert can_access_google_page("some address") == expected_result
