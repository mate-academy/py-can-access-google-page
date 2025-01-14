import pytest
from unittest import mock


from app.main import can_access_google_page


@pytest.mark.parametrize("valid_url, has_connection, expected", [
    pytest.param(True, True, "Accessible",
                 id="URL is valid, Internet connection is available"),
    pytest.param(False, True, "Not accessible",
                 id="URL is not valid, internet connection is available"),
    pytest.param(True, False, "Not accessible",
                 id="URL is valid, no internet connection"),
    pytest.param(False, False, "Not accessible",
                 id="URL is not valid, no internet connection"),
])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_url: str,
        mock_has_connection: str,
        valid_url: str,
        has_connection: str,
        expected: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_has_connection.return_value = has_connection
    result = can_access_google_page("https://www.google.com")
    assert result == expected
