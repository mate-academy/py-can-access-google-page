import pytest

from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,valid_url,internet,result",
    [
        ("https://www.google.com.ua", True, True, "Accessible"),
        ("https://www.google.com.ua", True, False, "Not accessible"),
        ("https://www.gooogle.com.ua", False, True, "Not accessible"),
        ("https://www.gooogle.com.ua", False, False, "Not accessible"),
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_valid_url_and_connection_exists(
        mocked_valid_url: mock.MagicMock,
        mocked_has_internet: mock.MagicMock,
        url: str, valid_url: bool, internet: bool, result: str
) -> None:
    mocked_valid_url.return_value = valid_url
    mocked_has_internet.return_value = internet
    assert can_access_google_page(url) == result
