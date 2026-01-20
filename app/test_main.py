# import pytest
from unittest.mock import patch
from app.main import can_access_google_page


# Mock functions
def mock_valid_google_url(url: str) -> bool:
    return url in ["https://www.google.com", "http://www.google.com"]


def mock_has_internet_connection() -> bool:
    from datetime import datetime
    current_time = datetime.now().time()
    return (datetime.strptime(
        "06:00:00", "%H:%M:%S").time()
        <= current_time
        <= datetime.strptime(
        "22:59:59", "%H:%M:%S").time())


# Test cases
@patch("app.main.valid_google_url", side_effect=mock_valid_google_url)
@patch("app.main.has_internet_connection",
       side_effect=mock_has_internet_connection
       )
def test_can_access_google_page(
        mock_valid_url: str,
        mock_internet_connection: str
) -> None:
    assert can_access_google_page("https://www.google.com") == "Accessible"
    assert can_access_google_page("http://www.google.com") == "Accessible"
    assert (can_access_google_page("https://www.invalidurl.com")
            == "Not accessible")
    assert (can_access_google_page("http://www.invalidurl.com")
            == "Not accessible")


# if __name__ == "__main__":
#     pytest.main(["-v", "app/test_main.py"])
