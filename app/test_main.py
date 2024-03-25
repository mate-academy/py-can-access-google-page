from unittest import mock

import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "internet_connection,valid_url,expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, False, "Not accessible"),
        ([], " ", "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock,
        internet_connection: bool,
        valid_url: bool,
        expected_result: str
) -> None:
    mocked_valid_google_url.return_value = internet_connection
    mocked_has_internet_connection.return_value = valid_url
    assert can_access_google_page("https://www.google.com") == expected_result
