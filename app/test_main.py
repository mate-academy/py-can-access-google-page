import pytest
from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "url,has_connection,valid_url,expected_result",
    [
        pytest.param(
            "https://www.google.com",
            False,
            True,
            "Not accessible"
        ),
        pytest.param(
            "https://www.bing.com",
            True,
            False,
            "Not accessible"
        ),
        pytest.param(
            "https://www.yahoo.com",
            True,
            True,
            "Accessible"
        ),
    ],
    ids=[
        "Not accessible - connection failed",
        "Not accessible - invalid url",
        "Accessible - connection established and url is valid"
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_has_internet_connection: callable,
        mocked_valid_google_url: callable,
        url: str,
        has_connection: bool,
        valid_url: bool,
        expected_result: str
) -> None:
    mocked_has_internet_connection.return_value = has_connection
    mocked_valid_google_url.return_value = valid_url
    assert can_access_google_page(url) == expected_result
