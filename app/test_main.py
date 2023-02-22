from unittest.mock import patch
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=["test for correct url and right time of the day",
         "test for incorrect url and right time of the day",
         "test for correct url and wrong time of the day",
         "test for incorrect url and wrong time of the day"]
)
@patch("app.main.valid_google_url")
@patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: bool,
        mock_has_internet_connection: bool,
        valid_google_url: bool,
        has_internet_connection: bool,
        result: str

) -> None:
    mock_valid_google_url.return_value = valid_google_url
    mock_has_internet_connection.return_value = has_internet_connection
    assert can_access_google_page("google.com") == result
