from unittest.mock import patch
from pytest import mark, param
from app.main import can_access_google_page


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
@mark.parametrize(
    "internet_connection, valid_url, expected_result",
    [
        param(True, True, "Accessible", id="Connected"),
        param(True, False, "Not accessible", id="No internet connection"),
        param(False, True, "Not accessible", id="Invalid URL"),
        param(False, False, "Not accessible", id="Invalid Url, no connect"),
    ]
)
def test_connection_and_url(
        mock_has_internet_connection: bool,
        mock_valid_google_url: bool,
        internet_connection: bool,
        valid_url: bool,
        expected_result: str
) -> None:
    mock_has_internet_connection.return_value = internet_connection
    mock_valid_google_url.return_value = valid_url

    result = can_access_google_page("http://www.google.com/")
    assert result == expected_result
