from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.requests.get")
def test_can_access_google_page(mock_requests_get: patch) -> None:
    mock_response = type("MockResponse", (), {"status_code": 200})
    mock_requests_get.return_value = mock_response

    with patch("app.main.has_internet_connection", return_value=True):
        result = can_access_google_page("http://www.google.com")
        assert result == "Accessible"

        mock_requests_get.return_value = type(
            "MockResponse", (), {"status_code": 404}
        )
        result = can_access_google_page("http://www.invalidurl.com")
        assert result == "Not accessible"

        with patch("app.main.has_internet_connection", return_value=False):
            result = can_access_google_page("http://www.google.com")
            assert result == "Not accessible"
