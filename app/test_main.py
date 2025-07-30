import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_internet, expected",
    [
        (True, True, "Accessible"),
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page_param(
        mocked_internet: mock.MagicMock,
        mocked_valid_url: mock.MagicMock,
        valid_url: bool,
        has_internet: bool,
        expected: str
) -> None:
    mocked_valid_url.return_value = valid_url
    mocked_internet.return_value = has_internet
    assert can_access_google_page("") == expected
