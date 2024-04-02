import pytest
from unittest.mock import patch, Mock
from app import main


@pytest.mark.parametrize(
    "url, valid_url, internet_connection, expected_result", [
        ("https://www.google.com", True, True, "Accessible"),
        ("https://www.invalidurl.com", False, True, "Not accessible"),
        ("https://www.google.com", True, False, "Not accessible"),
        ("https://www.google.com", False, False, "Not accessible")
    ])
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_has_internet_connection: Mock,
        mock_valid_google_url: Mock,
        url: str,
        valid_url: bool,
        internet_connection: bool,
        expected_result: str) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_connection
    result: str = main.can_access_google_page(url)
    assert result == expected_result


if __name__ == "__main__":
    import subprocess
    subprocess.check_call(["pip", "install", "requests"])
