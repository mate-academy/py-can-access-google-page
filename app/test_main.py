from app.main import can_access_google_page
import pytest
from unittest.mock import patch


@pytest.mark.parametrize("mock_url, mock_connect, result",
                         [
                            (True, True, "Accessible"),
                            (False, True, "Not accessible"),
                            (True, False, "Not accessible"),
                            (False, False, "Not accessible")
                         ])
def test_can_access_google_page(mock_url: str,
                                mock_connect: str, result: str) -> None:
    with patch("app.main.valid_google_url", return_value=mock_url),\
        patch("app.main.has_internet_connection", return_value=mock_connect):
        assert can_access_google_page("https://google.com") == result
