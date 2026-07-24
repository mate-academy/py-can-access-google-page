from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,internet_connection,expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "accessible with valid url and internet connection",
        "not accessible without internet connection",
        "not accessible with invalid url",
        "not accessible without valid url and connection",
    ],
)
@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page(
    mock_valid_google_url: mock.MagicMock,
    mock_has_internet_connection: mock.MagicMock,
    valid_url: bool,
    internet_connection: bool,
    expected: str,
) -> None:
    mock_valid_google_url.return_value = valid_url
    mock_has_internet_connection.return_value = internet_connection
    assert can_access_google_page("https://www.google.com") == expected, (
        f"Should return '{expected}' when url validity is "
        f"{valid_url} and internet connection is {internet_connection}"
    )
