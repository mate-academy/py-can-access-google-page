import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "has_connection, valid_url, expected_result",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "Connected, Valid URL",
        "Connected, Invalid URL",
        "No connection, Valid URL",
        "No connection, Invalid URL",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_url: mock,
        mocked_has_connection: mock,
        valid_url: bool,
        has_connection: bool,
        expected_result: str,
) -> None:
    mocked_valid_url.return_value = valid_url
    mocked_has_connection.return_value = has_connection
    assert can_access_google_page("google.com") == expected_result
