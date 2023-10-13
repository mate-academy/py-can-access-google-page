import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url, has_internet_connection, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ])
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
    mock_valid_google_url: bool,
    mock_has_internet_connection: bool,
    func_valid_google_url: bool,
    func_has_internet_connection: bool,
    expect_result: bool
) -> None:
    mock_valid_google_url.return_value = func_valid_google_url
    mock_has_internet_connection.return_value = func_has_internet_connection
    result = can_access_google_page("https://www.google.com")
    assert result == expect_result
