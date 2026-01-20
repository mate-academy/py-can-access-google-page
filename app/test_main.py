from unittest import mock
import pytest

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_google_url,has_internet_connection,expected_result",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ],
    ids=[
        "should return 'Accessible' with all function is True",
        "should return 'Not accessible' without `valid_google_url`",
        "should return 'Not accessible' without `has_internet_connection`",
        "should return 'Not accessible' with all function is False",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_google_url: mock.MagicMock,
        mocked_has_internet_connection: mock.MagicMock,
        valid_google_url: bool,
        has_internet_connection: bool,
        expected_result: str
) -> None:
    mocked_valid_google_url.return_value = valid_google_url
    mocked_has_internet_connection.return_value = has_internet_connection

    assert can_access_google_page("https://www.google.com/") == expected_result
