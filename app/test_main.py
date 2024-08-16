import pytest
from unittest import mock
from app.main import can_access_google_page


@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
@pytest.mark.parametrize(
    "mocked_valid_url_return, "
    "mocked_has_internet_return, "
    "url, "
    "expected_result",
    [
        (True, True, "https://www.google.com", "Accessible"),
        (True, False, "https://www.google.com", "Not accessible"),
        (False, True, "https://www.invalidurl.com", "Not accessible"),
        (False, False, "https://www.invalidurl.com", "Not accessible"),
    ]
)
def test_can_access_google_page(
        mocked_has_internet: mock.MagicMock,
        mocked_valid_url: mock.MagicMock,
        mocked_valid_url_return: bool,
        mocked_has_internet_return: bool,
        url: str,
        expected_result: str
) -> None:
    mocked_valid_url.return_value = mocked_valid_url_return
    mocked_has_internet.return_value = mocked_has_internet_return
    result = can_access_google_page(url)
    assert result == expected_result
