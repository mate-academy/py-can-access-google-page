import pytest
from app.main import can_access_google_page
from unittest.mock import patch


@pytest.mark.parametrize("input_url,expected,is_valid_url,has_connection", [
    pytest.param("https://google.com", "Accessible", True, True,
                 id="Should return Accessible "
                    "if url and connection are valid"),
    pytest.param("https://google.com", "Not accessible", True, False,
                 id="Should return Not accessible "
                    "if there is no connection"),
    pytest.param("https://validgoogle.com", "Not accessible", False, True,
                 id="Should return Not accessible "
                    "if url is invalid"),
    pytest.param("https://gle.com", "Not accessible", False, False,
                 id="Should return Not accessible "
                    "if url and connection are not valid"),
])
def test_can_access_google_page(input_url: str,
                                expected: str,
                                is_valid_url: bool,
                                has_connection: bool
                                ) -> None:
    with patch("app.main.valid_google_url") as mock_valid_url, \
         patch("app.main.has_internet_connection") as mock_i_connection:
        mock_valid_url.return_value = is_valid_url
        mock_i_connection.return_value = has_connection
        assert can_access_google_page(input_url) == expected
