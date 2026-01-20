import pytest
from unittest.mock import patch
from app.main import can_access_google_page

@pytest.mark.parametrize("valid_url, has_connection, expected", [
    (True, True, "Accessible"),   # Коректна URL і є інтернет
    (True, False, "Not accessible"),  # Коректна URL, але немає інтернету
    (False, True, "Not accessible"),  # Некоректна URL, але є інтернет
    (False, False, "Not accessible"),  # Некоректна URL і немає інтернету
])
def test_can_access_google_page(valid_url, has_connection, expected):
    with patch("app.main.valid_google_url", return_value=valid_url), \
         patch("app.main.has_internet_connection", return_value=has_connection):
        assert can_access_google_page("https://google.com") == expected
