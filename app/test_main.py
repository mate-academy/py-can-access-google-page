import pytest
from unittest.mock import patch
from app.main import can_access_google_page



@pytest.mark.parametrize(
    "validation,internet,expected_return",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
def test_output_from_valid_url_and_network(validation: bool,
                                           internet: bool,
                                           expected_return: str) -> None:

    with patch("app.main.valid_google_url", return_value=validation), \
        patch("app.main.has_internet_connection", return_value=internet):

        result = can_access_google_page("https://google.com")
        assert result == expected_return
