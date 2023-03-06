import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url_result,"
    "has_internet_connection_result,"
    "result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mock_valid_google_url: mock,
        mock_has_internet_connection: mock,
        valid_google_url_result: bool,
        has_internet_connection_result: bool,
        result: str
) -> None:
    mock_valid_google_url.return_value = valid_google_url_result
    mock_has_internet_connection.return_value = has_internet_connection_result
    assert can_access_google_page("https://www.google.com") == result
