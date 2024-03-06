import pytest
from unittest.mock import patch, MagicMock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "test_valid_link, test_has_internet_connection, expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_can_access_google(
        test_valid_link: bool,
        test_has_internet_connection: bool,
        expected_result: str
) -> None:
    with patch("app.main.valid_google_url",
               MagicMock(return_value=test_valid_link)):
        with patch("app.main.has_internet_connection",
                   MagicMock(return_value=test_has_internet_connection)):
            result = can_access_google_page("https://www.google.com")
            assert result == expected_result
