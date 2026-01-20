from unittest import mock
import pytest
from app.main import can_access_google_page

URL = "https://google.com"


@pytest.mark.parametrize(
    "url,valid_url,has_connection,excepted",
    [
        pytest.param(URL, True, False, "Not accessible"),
        pytest.param(URL, False, True, "Not accessible"),
        pytest.param(URL, True, True, "Accessible"),
        pytest.param(URL, False, False, "Not accessible"),
    ],
    ids=[
        "Valid url without internet",
        "Has internet connetion, bad url",
        "Valid url and internet connection",
        "Bad url without internet"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_url: callable,
        mocked_internet_connection: callable,
        url: str,
        valid_url: bool,
        has_connection: bool,
        excepted: str
) -> None:
    mocked_valid_url.return_value = valid_url
    mocked_internet_connection.return_value = has_connection
    assert can_access_google_page(url) == excepted
