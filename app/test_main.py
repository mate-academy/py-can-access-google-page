import pytest
from unittest.mock import patch
import app.main


@pytest.mark.parametrize(
    "valid_google_url,has_internet_connection,result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ],
    ids=[
        "Should be not accessible when there is no internet connection",
        "Should be not accessible when url is invalid",
        "Should be not accessible when both checks are False",
        "Should be accessible when there is internet connection & url is valid"
    ]
)
@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page(mock_valid_google_url: callable,
                                mock_has_internet_connection: callable,
                                valid_google_url: bool,
                                has_internet_connection: bool,
                                result: str) -> None:
    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet_connection.return_value = has_internet_connection
    assert app.main.can_access_google_page("google.com") == result
