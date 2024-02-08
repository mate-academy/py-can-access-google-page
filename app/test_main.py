import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url, valid_url, internet_connection, expected_result",
    [
        ("https://google.com", True, True, "Accessible"),
        ("google.com", False, True, "Not accessible"),
        ("http://google.com", True, False, "Not accessible"),
        ("google.com", False, False, "Not accessible"),
    ],
    ids=[
        "Should return 'Accessible' when valid url "
        "and has internet connection",
        "Should return 'Not accessible' when not valid url",
        "Should return 'Not accessible' when hasn't internet connection",
        "Should return 'Not accessible' when not valid url "
        "and hasn't internet connection",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_valid_url: mock,
    mock_has_internet_connection: mock,
    url: str,
    valid_url: bool,
    internet_connection: bool,
    expected_result: str
) -> None:
    mock_valid_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("http://google.com") == expected_result
