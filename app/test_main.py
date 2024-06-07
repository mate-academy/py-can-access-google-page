import pytest
from unittest.mock import patch

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "mock_internet, mock_valid_url, expected_result",
    [
        pytest.param(True, True, "Accessible",
                     id="test_can_access_google_page"),
        pytest.param(False, True, "Not accessible",
                     id="test_cannot_access_due_to_internet_connection"),
        pytest.param(True, False, "Not accessible",
                     id="test_cannot_access_due_to_invalid_url"),
        pytest.param(False, False, "Not accessible",
                     id="test_not_valid_url_and_bad_internet_connection")
    ]
)
def test_can_access_google_page(
        mock_internet: None,
        mock_valid_url: None,
        expected_result: bool
) -> None:
    with patch("app.main.valid_google_url", return_value=mock_valid_url):
        with patch(
                "app.main.has_internet_connection", return_value=mock_internet
        ):
            assert can_access_google_page(
                "https://www.google.com"
            ) == expected_result
