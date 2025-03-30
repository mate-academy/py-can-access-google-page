import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "response, current_time, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mock_valid_google_url: bool,
        mock_has_internet_connection: bool,
        response: bool,
        current_time: bool,
        expected_result: str
) -> None:
    url = "https://www.google.com.ua/"
    mock_valid_google_url.return_value = response
    mock_has_internet_connection.return_value = current_time
    assert can_access_google_page(url) == expected_result
