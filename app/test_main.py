import pytest

from unittest import mock

from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url,connection,result",
    [
        (True, False, "Not accessible"),
        (False, True, "Not accessible"),
        (False, False, "Not accessible"),
        (True, True, "Accessible")
    ],
    ids=[
        "You have unstable internet connection",
        "You have invalid URL",
        "You have invalid url and unstable internet connection",
        "You have an access",
    ]
)
@mock.patch("app.main.valid_google_url")
@mock.patch("app.main.has_internet_connection")
def test_can_access_google_page(
        mocked_valid_url: mock,
        mocked_connection: mock,
        valid_url: bool,
        connection: bool,
        result: str
) -> None:
    url = "www.google.com"
    mocked_valid_url.return_value = valid_url
    mocked_connection.return_value = connection
    assert can_access_google_page(url) == result
