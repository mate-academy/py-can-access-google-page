import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_internet_connection,valid_google_url,result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible")
    ],
    ids=[
        "Valid to access the Google home page and it has internet connection",
        "Check URL",
        "Check internet connection",
        "Check URL and internet connection"
    ]
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
        mock_has_internet_connection: mock,
        mock_main_valid_google_url: mock,
        valid_google_url: bool,
        has_internet_connection: bool,
        result: str
) -> None:
    mock_has_internet_connection.return_value = has_internet_connection
    mock_main_valid_google_url.return_value = valid_google_url
    assert can_access_google_page("https://google.com") == result
